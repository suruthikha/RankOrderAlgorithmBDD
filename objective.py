def averageRank(R, A_arr):
    ranks = []
    unmatched = []
    for resident in range(len(R)):
        if A_arr[resident] is None:
            unmatched.append(resident)
            continue
        ranks.append(R[resident].index(A_arr[resident] + 1) + 1)

    if unmatched:
        print(f"Warning: {len(unmatched)} resident(s) unmatched: {unmatched}")

    averageRrank = sum(ranks) / len(ranks) if ranks else float("nan")
    print("Average Rank:", averageRrank)
    return averageRrank
