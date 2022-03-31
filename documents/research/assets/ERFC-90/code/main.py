import utils


def run(contract, methodIds, start_block, end_block):
    '''Detects potential Wash trades for a marketplace's contract'''

    transactions = utils.get_all_transactions(
        contract, 
        start_block, 
        end_block
    )

    wtd0_count, wtd1_cas, total = 0, [], 0

    for  tx in transactions:

        if tx['input'][:10] in methodIds:

            status, logs = utils.get_logs(tx['hash'])

            if status != 1: # Reverted transaction
                continue

            nft_contract, token_id, A, B = utils.parse_logs(logs)

            if A == None or B == None: # not a standard ERC721 
                continue

            associates_A = utils.get_associates(A)
            associates_B = utils.get_associates(B)

            wtd0_count += int(
                utils.wtd0(A, B, associates_A, associates_B)
            )
            wtd1_cas.append(
                utils.wtd1(A, B, associates_A, associates_B)
            )

            total += 1
        
    return (wtd0_count, wtd1_cas, total)


WYVERN_V1 = '0x7Be8076f4EA4A4AD08075C2508e481d6C946D12b'

ranges = [
    [6652089, 6652239],
    [7486211, 7486311],
    [7704798, 7704898],
]

for start_block, end_block in ranges:

    print(run(WYVERN_V1, ['0xab834bab'], start_block, end_block))

