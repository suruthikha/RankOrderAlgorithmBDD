### Set up random seed

import random
random.seed(42)

def Random(R, C, test_mode):
    A_arrR = [0 for r in R]
    
    for resident in random.sample(list(R.keys()), len(R)):
        hospital = random.choice([h for h in remaining_Ccopy if remaining_Ccopy[h] > 0])
        A_arrR[resident].append(hospital)
        remaining_Ccopy[hospital] -= 1
