#**Goal of this repository**:
This package adapts the Resident-Oriented Gale-Shapley (RGS) algorithm/Roth-Peranson algorithm to match entities across two sets of groups using one-sided preferences (otherwise known as a non-bipartite matching problem [1]). One example use case is assigning doctors to hospitals, taking into account doctors’ preferences only. The following constraints detail the case our algorithm handles:

#**Mathematical and model assumptions**:
1. Every resident ranks all hospitals.
2. Every resident ranks each hospital a different rank.
3. Each hospital is listed once in a resident’s preference list.
4. Per one-sided matching, hospitals may not contain preferences.
5. The total hospital capacity (the sum capacity across all hospitals) is greater than or equivalent to the total number of doctors.
6. The capacity of a hospital can be 0 but not negative, as long as the total hospital capacity meets the assumption #5.
7. Note that we will not test strategy-proofness for our case, as not only can there be no hospital-resident algorithm that is both stable and strategy both for hospitals [1], we assume residents have no need to strategize their preference lists to bias outcome because there are no hospital preferences.

#**RGS/Roth-Peranson algorithms**:
+ At the first step of the RGS algorithm, each doctor applies to their first-choice hospital.  For each hospital h<sub>j</sub>, the c<sub>j</sub> acceptable applicants who have the highest ranks according to h<sub>j</sub>’s preference list (or all acceptable applicants if there are fewer than c<sub>j</sub>) are placed on the waiting list of h<sub>j</sub>. All other applicants are rejected [1].
+ At the l-th step of the RGS algorithm, rejected applicants at step l-1 apply to their next best acceptable hospital. For each hospital h<sub>j</sub>, the c<sub>j</sub> acceptable applicants among the new applicants and those on the waiting list who have the highest ranks according to h<sub>j</sub>’s preference list (or all acceptable applicants if there are fewer than c<sub>j</sub>) are placed on the waiting list of hj<sub>j</sub>, and all others are rejected [1].
+ The Roth-Peranson algorithm follows the same steps as the RGS algorithm, but adds an additional step: Acceptances are tentative until the termination of the algorithm, such that a hospital may let go of a previously accepted student to make room for a higher ranked doctor in a later round of proposals. This algorithm is used by the National Resident Matching Program [2].

#**Our algorithm**:
Accordingly, we modified the RGS/Roth-Peranson algorithms such that we only take into account doctors’ preferences for hospitals. Because we do not take into account hospital preferences, random assignment will be used in cases where there are more applicants to a particular hospital than its capacity, and once doctors are assigned to a hospital, it is permanent. We bold the significant design decisions that account for algorithmic decisions in the absence of hospital preference below:
+ At the first step of our algorithm, each doctor applies to their first-choice hospital.  For each hospital h<sub>j</sub>, **if there are fewer than c<sub>j</sub> applicants, all of these applicants are accepted into h<sub>j</sub>. If there are more than c<sub>j</sub> applicants, c<sub>j</sub> applicants are randomly selected from this pool and accepted into h<sub>j</sub>. All other applicants are rejected.**
+ At the l-th step of our algorithm, rejected applicants at step l-1 apply to their next-choice hospital. For each hospital h<sub>j</sub>, **if there are fewer than c<sub>j</sub> applicants, all of these applicants are accepted into h<sub>j</sub>. If there are more than c<sub>j</sub> applicants, c<sub>j</sub> applicants are randomly selected from this pool and accepted into hj. All other applicants are rejected.**
+ **All acceptances into hospitals are final; unlike the Roth-Peranson algorithm, a hospital cannot let go a previously accepted student.**
