# **Goal of This Repository**:
This package adapts the Resident-Oriented Gale-Shapley (RGS) algorithm/Roth-Peranson algorithm to match entities across two sets of groups using one-sided preferences (otherwise known as a non-bipartite matching problem [1]). One example use case is assigning doctors to hospitals, taking into account doctors’ preferences only. The following constraints detail the case our algorithm handles:

# **Mathematical and Model Assumptions**:
1. Every doctor ranks all hospitals.
2. Every doctor ranks each hospital a different rank.
3. Each hospital is listed once in a doctor’s preference list.
4. Per one-sided matching, hospitals may not contain preferences.
5. The total hospital capacity (the sum capacity across all hospitals) is greater than or equivalent to the total number of doctors.
6. The capacity of a hospital can be 0 but not negative, as long as the total hospital capacity meets the assumption #5.
7. Note that we will not test strategy-proofness for our case, as not only can there be no hospital-doctor algorithm that is both stable and strategy both for hospitals [1], we assume doctors have no need to strategize their preference lists to bias outcome because there are no hospital preferences.

# **RGS/Roth-Peranson Algorithms**:
+ At the first step of the RGS algorithm, each doctor applies to their first-choice hospital.  For each hospital h<sub>j</sub>, the c<sub>j</sub> acceptable applicants who have the highest ranks according to h<sub>j</sub>’s preference list (or all acceptable applicants if there are fewer than c<sub>j</sub>) are placed on the waiting list of h<sub>j</sub>. All other applicants are rejected [1].
+ At the l-th step of the RGS algorithm, rejected applicants at step l-1 apply to their next best acceptable hospital. For each hospital h<sub>j</sub>, the c<sub>j</sub> acceptable applicants among the new applicants and those on the waiting list who have the highest ranks according to h<sub>j</sub>’s preference list (or all acceptable applicants if there are fewer than c<sub>j</sub>) are placed on the waiting list of hj<sub>j</sub>, and all others are rejected [1].
+ The Roth-Peranson algorithm follows the same steps as the RGS algorithm, but adds an additional step: Acceptances are tentative until the termination of the algorithm, such that a hospital may let go of a previously accepted student to make room for a higher ranked doctor in a later round of proposals. This algorithm is used by the National Resident Matching Program [2].

# **Our Algorithm**:
Accordingly, we modified the RGS/Roth-Peranson algorithms such that we only take into account doctors’ preferences for hospitals. Because we do not take into account hospital preferences, random assignment will be used in cases where there are more applicants to a particular hospital than its capacity, and once doctors are assigned to a hospital, it is permanent. We bold the significant design decisions that account for algorithmic decisions in the absence of hospital preference below:
+ At the first step of our algorithm, each doctor applies to their first-choice hospital.  For each hospital h<sub>j</sub>, **if there are fewer than c<sub>j</sub> applicants, all of these applicants are accepted into h<sub>j</sub>. If there are more than c<sub>j</sub> applicants, c<sub>j</sub> applicants are randomly selected from this pool and accepted into h<sub>j</sub>. All other applicants are rejected.**
+ At the l-th step of our algorithm, rejected applicants at step l-1 apply to their next-choice hospital. For each hospital h<sub>j</sub>, **if there are fewer than c<sub>j</sub> applicants, all of these applicants are accepted into h<sub>j</sub>. If there are more than c<sub>j</sub> applicants, c<sub>j</sub> applicants are randomly selected from this pool and accepted into hj. All other applicants are rejected.**
+ **All acceptances into hospitals are final**; unlike the Roth-Peranson algorithm, a hospital **cannot let go a previously accepted student.**

# **Baseline Algorithm**:
To compare the performance of our algorithm, we chose a baseline algorithm of random feasible assignment [3], where doctors were randomly assigned to hospitals only considering hospital capacity.

# **Comparison of Metrics**:
Two metrics were calculated and considered to evaluate the performance and efficiency of the two algorithms; average preference of the final assignment and the time taken to provide the assignments.

The table below shows the metrics when dealing with a variety of combinations between the number of doctors and hospitals. The results show that as the number of doctors and hospitals increased, the computation time taken increased across both methods, however the random method consistently stayed around 0-1 ms and was computationally faster compared to the RGS computation time. 

As for the average rank, the RGS algorithm showed a significantly  lower average rank than the random algorithm, meaning that more doctors got their top preferences or preferences close to the top. This makes sense as the random algorithm did not take doctor preferences into account. 

Overall, while the random algorithm was computationally faster, the RGS algorithm was better in providing doctors assignments they can be happy with. 

| Number of Doctors | Number of Hospitals | RGS Metrics | Random Metrics |
| :---: | :---: | :--- | :--- |
| 50 | 5 | Average Rank: 1.06<br> Time Taken (ms): 5 | Average Rank: 2.94<br> Time Taken (ms): 0 |
| 100 | 10 | Average Rank: 1.24<br> Time Taken (ms): 29 | Average Rank: 5.54<br> Time Taken (ms): 0 |
| 250 | 15 | Average Rank: 1.11<br> Time Taken (ms): 48 | Average Rank: 2.94<br> Time Taken (ms): 0 |
| 50 | 5 | Average Rank: 1.13<br> Time Taken (ms): 72 | Average Rank: 12.78<br> Time Taken (ms): 0 |
| 50 | 5 | Average Rank: 1.18<br> Time Taken (ms): 121 | Average Rank: 25.53<br> Time Taken (ms): 1 |

# **Limitations**:
One possible limitation is the efficiency of the algorithm. Our algorithm takes significantly longer than random feasible assignment with increasing input size, and while the computation only takes milliseconds to run with 500 doctors and 50 hospitals, this may substantially increase with larger inputs. By nature of the problem, the proposed algorithm is limited in applicability due to its inability to consider multiple facets of doctor-hospital matching in real life, including (but not limited to): hospital preferences, quotas hospitals have to fill for certain departments, and other factors that make certain doctors more well suited for certain hospitals over others.

# **Possible Extensions**:
Within the scope of our problem, one possible extension to improve our algorithm is to improve computational efficiency by utilizing NumPy arrays and operations.

# **Other Notes**:
We provide example inputs where R is a vector of doctors’ preferences (each hospital is labeled as a number, and preferences match the index of the vector), and C is a vector of hospitals' capacities. Our code checks whether the input meets the assumption that total hospital capacity is equal to or greater than the total number of doctors. However, it should be noted that input must specifically match the examples; our code does not handle hospitals being labeled as ‘A’, ‘B’, ‘C’, for example.

# **Team Contributions**:
Mina Jung
+ Conducted literature review and research on RGS/Roth-Peranson algorithms
+ Created conceptual modification of RGS/Roth-Peranson algorithms to take into account doctors’ preferences only
+ Coded initial draft of the modified RGS/Roth-Peranson algorithm (rankorder_shared_MJ.ipynb)
+ Generated example inputs to test algorithm
+ Wrote and edited README file
Emily Sun
+ Learned about mathematical foundation behind RGS
+ First draft of repo goal and assumptions for the README
+ Standardize input formatting and separate functions for printing
+ Move .ipynb functions to .py files
+ Bug fixes to helper print functions, RGS algorithm, and average rank method
+ Run tests on RGS_test.py
Suruthikha Vijay
+ Worked on editing, debugging, and testing the code in the ‘rankOrderWithEverything1.ipynb’ file
+ Created a random input generator method to generate doctor preferences given a number of doctors and a number of hospitals
+ Created a random assignment algorithm that only takes into account hospital capacity
+ Created an average rank method that calculates the average rank of the doctor assignments
+ Tested the code with the example inputs as well as the random input generator
+ Collected the average rank and computation time of each method for each set of inputs for further analysis and comparison
+ Edited README file

# **References**:
[1] B. Klaus, D. Manlove, and F. Rossi, “Matching under Preferences,” 2014. Accessed: Sept. 10, 2026. [Online]. Available: https://eprints.gla.ac.uk/107411/1/107411.pdf
[2] M. Maaz, “A Primer on the Game Theory Behind the National Resident Matching Program for the Medical Educator and Student,” Medical Science Educator, Apr. 2020, doi: 10.1007/s40670-020-00955-8.
[3] P. A. Krokhmal and P. M. Pardalos, “Random assignment problems,” European Journal of Operational Research, vol. 194, no. 1, pp. 1–17, Apr. 2009, doi: 10.1016/j.ejor.2007.11.062.
