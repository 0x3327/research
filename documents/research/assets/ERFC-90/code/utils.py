import time, json, requests
from web3 import Web3

config = {
    "alchemy-url" : "https://eth-mainnet.alchemyapi.io/v2/yo4qrfb-KgIuV2wOWhcNTsL9OgaBbZPc",
    "etherscan-api-key": 'DTTYB2BNYEHDG4C8TYF7USTS3MAT99R399',
}

web3 = Web3(Web3.HTTPProvider(config['alchemy-url']))

def get_all_transactions(address, start_block = 0, end_block = 19999999):
    '''Gets all transactions using Etherscan API for the provided address'''
    transactions = []

    while True:
        time.sleep(5)
        result = requests.get(
            'https://api.etherscan.io/api?module=account&action=txlist' +
            f'&address={address}' +
            f'&startblock={start_block}' +
            f'&endblock={end_block}' +
            f'&offset={1_000}' +
            f'&sort={"asc"}' +
            f'apikey={config["etherscan-api-key"]}'
        ).json()['result']

        transactions += result

        if len(result) < 1_000:
            break

        start_block = int(result[-1]["blockNumber"]) + 1


    return transactions

def is_EOA(address):
    '''Returns true if the address belongs to an Externally Owned Account'''

    try:
        _address = Web3.toChecksumAddress(address)
        return web3.eth.getCode(_address) == b""
    except:
        return False

def get_associates(address):
    '''Returns a set of all account with which the provided addresses interacted with'''

    transactions = get_all_transactions(address)

    associates = set()
    for tx in transactions:
        if tx['from'] != address:
            associates.update([tx['from']])
        if tx['to'] != address:
            associates.update([tx['to']])

    return associates

def get_logs(tx_hash):
    '''Gets the logs from the transaction receipt of the tx_hash'''

    tx_receipt = web3.eth.get_transaction_receipt(tx_hash)
 
    return tx_receipt['status'], tx_receipt['logs']

def parse_logs(logs):
    '''Returns the NFT contract's address, token id and addresses involved in the trade'''

    TRANSFER_TOPIC = "0xddf252ad1be2c89b69c2b068fc378daa952ba7f163c4a11628f55a4df523b3ef"
    WRAPPED_ETH = "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2"

    nft_contracts, token_ids, _from, _to = [], [], None, None

    for ev in logs:

        if TRANSFER_TOPIC == ev["topics"][0].hex() and ev["address"] != WRAPPED_ETH:

            nft_contracts.append(ev["address"])

            bytecode = "".join([x.hex() for x in ev["topics"]]) + "".join(ev["data"])
            _from = "0x" + bytecode[66 : 66 * 2][-40:]
            _to = "0x" + bytecode[66 * 2 : 66 * 3][-40:]
            token_ids.append(int(bytecode[66 * 3 : 66 * 4][2:66], base=16))

    return nft_contracts, token_ids, _from, _to


def wtd0(A, B, associates_A, associates_B):
    '''WTD0 implementation'''

    return (A in associates_B) or (B in associates_A)

def wtd1(A, B, associates_A, associates_B):
    '''WTD1 implementation'''
    
    EOA_associates = []

    common_associates = associates_A.intersection(associates_B)
    for ca in common_associates:
        if is_EOA(ca):
            EOA_associates.append(ca)
        
    return EOA_associates