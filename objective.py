def averageRank(R, A_arr):
    A_Rank = [R[resident].index(A_arr[resident] + 1) + 1 for resident in range(len(R))]
    averageRrank = sum(A_Rank) / len(A_Rank)
    print("Average Rank:", averageRrank)
    return averageRrank
