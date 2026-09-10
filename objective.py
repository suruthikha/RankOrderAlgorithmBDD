from random import random

def averageRank(R, A_arr):
    if A_arr is None:
        print("No assignment possible")
        return float("nan")
    A_Rank = [R[resident].index(A_arr[resident] + 1) + 1 for resident in range(len(R))]
    averageRrank = sum(A_Rank) / len(A_Rank)
    print("Average Rank:", averageRrank)
    return averageRrank
