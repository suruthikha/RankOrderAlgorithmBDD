# ====================================================================
# Test 1

# Input: Resident preferences
# R in numpy array form
R = [[1,2,3],
     [1,2,3],
     [1,3,2],
     [3,1,2]]

# Original capacity
C = [2,1,1]

# We modify to store the results from previous hospitals.
A_arr = [[],[],[],[]]

# ====================================================================
# Test 2

# ====================================================================
# Test 3

# ====================================================================
# Run test
if __name__ == "__main__":
    A_arr = RGS(R, C, A_arr, test_mode=True) # Test 1
