# Imports

from baseline import _Random
from objective import averageRank
from RGS_algorithm import RGS
from time import time
import random

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
    print("Time for Algorithm:", RTime ,"microseconds")
    print("   ")
    milliRandomStart = int(time() * 1000)*1000
    A_arrR = _Random(R, C, test_mode=True)
    averageRank(R,A_arrR)
    milliRandomEnd = int(time() * 1000)*1000
    RTime = milliRandomEnd-milliRandomStart
    print("Time for Random Algorithm:", RTime ,"microseconds")

# ====================================================================
# Generator functions

def generate_large_input(n_doctors, n_hospitals, seed=None,
                          min_capacity=1, max_extra_capacity=3):
    """
    Parameters
    ----------
    n_doctors : int
        Number of residents/doctors to generate preferences for.
    n_hospitals : int
        Number of hospitals to generate capacities for.
    seed : int, optional
        RNG seed for reproducibility.
    min_capacity : int
        Capacity every hospital is guaranteed to start with, so no
        hospital is randomly left at 0 seats.
    max_extra_capacity : int
        Upper bound on extra random slack added per hospital on top of
        the minimum + doctor-covering allocation, so total capacity
        comfortably exceeds n_doctors rather than just equaling it.

    Returns
    -------
    R : list[list[int]]
        R[d] is doctor d's full ranked preference list over hospitals,
        1-indexed (1..n_hospitals), each hospital appearing exactly once.
    C : list[int]
        C[h] is hospital h's capacity.
    H : list[list[int]]
        Empty per-hospital applicant buckets: H[h] = [] for every hospital,
        the shape RGS expects at the start of round 1.
    """
    rng = random.Random(seed)

    # --- R: every doctor ranks every hospital exactly once ---
    hospitals = list(range(1, n_hospitals + 1))  # 1-indexed, matches notebook
    R = []
    for _ in range(n_doctors):
        prefs = hospitals[:]
        rng.shuffle(prefs)
        R.append(prefs)

    # --- C: random capacities guaranteed to sum to >= n_doctors ---
    C = [min_capacity] * n_hospitals
    remaining_needed = max(0, n_doctors - sum(C))
    for _ in range(remaining_needed):
        C[rng.randrange(n_hospitals)] += 1
    for h in range(n_hospitals):
        C[h] += rng.randint(0, max_extra_capacity)

    # --- H: empty applicant buckets, one per hospital ---
    H = [[] for _ in range(n_hospitals)]

    return R, C, H

def validate_input(R, C, n_doctors, n_hospitals):

    assert sum(C) >= n_doctors, "Total capacity is less than the number of doctors"
    for d, prefs in enumerate(R):
        assert len(prefs) == n_hospitals, f"Doctor {d} preference list has wrong length"
        assert sorted(prefs) == list(range(1, n_hospitals + 1)), (
            f"Doctor {d} preference list is missing a hospital or has a duplicate rank"
        )

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

    n_doctors = 5
    n_hospitals = 3

    R, C, H = generate_large_input(n_doctors, n_hospitals, seed=42)

    totalC = sum(C)
    print(f"Doctors: {n_doctors}, Hospitals: {n_hospitals}")
    print(f"Total capacity: {totalC} (needs >= {n_doctors})")
    print(f"Capacities (C): {C}")
    print(f"Sample doctor 0 preference list (R[0]): {R[0]}")
    print(f"Initial H (empty applicant buckets): {H}")
    print()

    validate_input(R, C, n_doctors, n_hospitals)
