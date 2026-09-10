# Imports

import baseline
from objective import averageRank
from RGS_algorithm import RGS

# ====================================================================
# Test 0: Input does not meet assumptions: total capacity < number of residents

R = [[3,2,1],
     [3,2,1],
     [3,2,1],
     [3,2,1]]

C = [1,1,1]

# ====================================================================
# Test 1: No residents have conflicting preferences

# Resident preferences
R = [[1,2,3],
     [3,1,2],
     [2,3,1]]

# Original hospital capacity
C = [1,1,1]

# ====================================================================
# Test 2: Some residents have conflicting preferences

# Resident preferences
R = [[1,2,3],
     [1,3,2],
     [2,3,1]]

# Original hospital capacity
C = [1,1,1]

# ====================================================================
# Test 3: More residents than number of hospitals

# Resident preferences
R = [[1,2,3],
     [1,2,3],
     [1,3,2],
     [3,1,2]]

# Original hospital capacity
C = [2,1,1]

# ====================================================================
# Test 4: Less residents than total capacity

R = [[3,2,1,4],
     [3,2,4,1],
     [2,1,4,3]]

C = [1,2,1]

# ====================================================================
# Test 5: Hospital with 0 capacity

# Resident preferences
R = [[1,2,3],
     [3,1,2],
     [2,3,1]]

# Original hospital capacity
C = [1,0,2]

# ====================================================================
# Test 6: Large dataset

R = [[]]

C = []

# ====================================================================
# Run test
if __name__ == "__main__":
    A_arr = RGS(R, C, A_arr, test_mode=True) # Test 1

    milliS = int(time() * 1000)*1000
    A_arr = RGS(R, C, A_arr, test_mode=True)
    averageRank(R,A_arr)
    milliEnd = int(time() * 1000)*1000
    RTime = milliEnd-milliS
    print("Time for Algorithm:", RTime ,"microseconds")

    milliRandomStart = int(time() * 1000)*1000
    A_arrR = RGS(R, C, A_arrR, test_mode=True)
    averageRank(R,A_arrR)
    milliRandomEnd = int(time() * 1000)*1000
    RTime = milliRandomEnd-milliRandomStart
    print("Time for Random Algorithm:", RTime ,"microseconds")
