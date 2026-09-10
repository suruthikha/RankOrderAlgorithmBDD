# Imports

from baseline import Random
from objective import averageRank
from RGS_algorithm import RGS
from time import time

# ====================================================================
# Test 0: Input does not meet assumptions: total capacity < number of residents

R0 = [[3,2,1],
     [3,2,1],
     [3,2,1],
     [3,2,1]]

C0 = [1,1,1]

# ====================================================================
# Test 1: No residents have conflicting preferences

# Resident preferences
R1 = [[1,2,3],
     [3,1,2],
     [2,3,1]]

# Original hospital capacity
C1 = [1,1,1]

# ====================================================================
# Test 2: Some residents have conflicting preferences

# Resident preferences
R2 = [[1,2,3],
     [1,3,2],
     [2,3,1]]

# Original hospital capacity
C2 = [1,1,1]

# ====================================================================
# Test 3: More residents than number of hospitals

# Resident preferences
R3 = [[1,2,3],
     [1,2,3],
     [1,3,2],
     [3,1,2]]

# Original hospital capacity
C3 = [2,1,1]

# ====================================================================
# Test 4: Less residents than total capacity

R4 = [[3,2,1,4],
     [3,2,4,1],
     [2,1,4,3]]

C4 = [1,2,1]

# ====================================================================
# Test 5: Hospital with 0 capacity

# Resident preferences
R5 = [[1,2,3],
     [3,1,2],
     [2,3,1]]

# Original hospital capacity
C5 = [1,0,2]

# ====================================================================
# Test 6: Large dataset

R6 = [[]]

C6 = []

# ====================================================================
# Timing function

def time_func(R, C):
    milliS = int(time() * 1000)*1000
    A_arr = RGS(R, C, test_mode=True)
    averageRank(R,A_arr)
    milliEnd = int(time() * 1000)*1000
    RTime = milliEnd-milliS
    '''
    print("Time for Algorithm:", RTime ,"microseconds")
    print("   ")
    milliRandomStart = int(time() * 1000)*1000
    A_arrR = Random(R, C, test_mode=True)
    averageRank(R,A_arrR)
    milliRandomEnd = int(time() * 1000)*1000
    RTime = milliRandomEnd-milliRandomStart
    '''
    print("Time for Random Algorithm:", RTime ,"microseconds")

# ====================================================================
# Run test
if __name__ == "__main__":
    time_func(R0, C0) # Test 0
    time_func(R1, C1) # Test 1
    time_func(R2, C2) # Test 2
    time_func(R3, C3) # Test 3
    time_func(R4, C4) # Test 4
    time_func(R5, C5) # Test 5
    time_func(R6, C6) # Test 6
