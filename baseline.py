### Set up random seed

import random
random.seed(42)

def Random(R, C, A_arrR, test_mode):
    for resident in random.sample(list(R.keys()), len(R)):
        hospital = random.choice([h for h in remaining_Ccopy if remaining_Ccopy[h] > 0])
        A_arrR[resident].append(hospital)
        remaining_Ccopy[hospital] -= 1
