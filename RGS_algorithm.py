from printing_helper import print_acc_rej
from printing_helper import print_A
from printing_helper import print_H
from printing_helper import print_C
from printing_helper import print_hosp
from printing_helper import print_app

### Set up the random seed

import random
random.seed(42)

### Subsequent Rounds

def RGS(R, C, A_arr, test_mode):

    # Convert to 0-based indexing
    R = [[i-1 for i in r] for r in R]

    # Remaining capacity
    remaining_C = C.copy()

    pref_round = 0
    current_applicants = list(range(len(R)))

    # Implicit way to run loop while current_applicants is NOT empty
    # We also assume that each resident's preference list is the same, hence why taking len(r1) would be sufficient
    while current_applicants and (pref_round<len(R[0])):

        # New H for this round
        H = [[],[],[]]

        # Build H from current applicants
        for resident, choices in enumerate(R):
            if resident in current_applicants:
                H[choices[pref_round]].append(resident)

        if test_mode:
           print(f"Hospital choices for round {pref_round+1}: ", end="")
           print_H(H)

        # Accept or reject applicants
        round_reject = []
        for hospital, applicants in enumerate(H):
            if len(applicants) > remaining_C[hospital]: # Too many applicants per capacity
                accepted = random.sample(applicants, remaining_C[hospital])
                rejected = [item for item in applicants if item not in accepted]
                round_reject += rejected
                if test_mode: print_acc_rej(hospital, accepted, rejected)
            else:
                accepted = applicants
                rejected = []
                if test_mode: print_acc_rej(hospital, accepted, rejected)
            for resident in accepted: # Separating consequences of decision
                A_arr[resident] = hospital
                remaining_C[hospital]-= 1

        if test_mode:
          print(f"Assignments for round {pref_round+1}: ", end="")
          print_A(A_arr)
          print(f"Rejections for round {pref_round+1}: ", end="")
          print_app(round_reject, end="\n")
          print(f"Remaining capacities for round {pref_round+1}: ", end="")
          print_C(remaining_C)

        # Update round
        current_applicants = round_reject
        pref_round += 1

    if test_mode:
        print(f"Final assignments: ", end="")
        print_A(A_arr)
        print(f"Final capacities: ", end="")
        print_C(remaining_C)

    return A_arr
