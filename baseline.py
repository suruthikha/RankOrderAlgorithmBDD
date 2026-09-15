### Set up random seed

import random
random.seed(42)

def _Random(R, C, test_mode=False):
    if sum(C) < len(R):
        print("Please read the README and make sure the number of doctors and hospitals are correct")
        return

    A_arrR = [None] * len(R)
    remaining_C = C.copy()

    residents = list(range(len(R)))
    random.shuffle(residents)

    hospitals_with_room = [h for h in range(len(C)) if remaining_C[h] > 0]
    for resident in residents:
        if not hospitals_with_room:
            if test_mode:
                print(f"Resident {resident} could not be placed — no capacity left anywhere")
            continue
        hospital = random.choice(hospitals_with_room)
        A_arrR[resident] = hospital
        remaining_C[hospital] -= 1
        if remaining_C[hospital] == 0:
            hospitals_with_room.remove(hospital)

    return A_arrR
