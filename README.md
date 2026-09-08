A package for solving resident hospital allocations

This package uses Resident-Oriented Gale-Shapley (RGS) Algorithm/Roth-Peranson Algorithm to solve certain cases of the issue of allocating entities across the bipartite group using one-sided preferences. One example of this in real life is assigning residents to hospitals. The below constraints detail the case our algorithm handles:

Mathematical and model assumptions:
Every resident ranks all hospitals.
Every resident ranks each hospital a different rank.
Each hospital is listed once in a resident’s preference list.
Per one-sided matching, hospitals may not contain preferences.
The total hospital capacity is at least the capacity of the doctors’.
Note that we will not test strategy-proofness for our case, as there can be no hospital resident algorithm that is both stable and strategy both for hospitals (Roth, 1986).

Accordingly, we modify the Roth-Peranson Algorithm.
	
Design decisions:
Because of one-sided matching, the other group, the hospitals, cannot contain preferences.
When resident preferences are treated the same, randomization is used to treat each resident equally.

Our algorithm:
Stability - a match where there are no unstable matches, which is defined as a match where a better one exists for either agent
Preferences are strict; given a choice, there is no indifference between options
Resident-Oriented Gale-Shapley (RGS) Algorithm/Roth-Peranson Algorithm
Students submit preference lists of residency positions and hospitals rank applicants. Students’ preference is prioritized.
First round: students propose to their first-choice hospital; Hospitals accept the top students from their proposers according to their own ranking of students, up to their quota, and reject the others. 
Rejected students go on to propose to their next preferred hospital, and so on. 
Acceptances are tentative until the termination of the algorithm, such that a hospital may let go of a previously accepted student to make room for a higher ranked student in a later round of proposals.
Because we don’t take into account hospital preferences, (a) more applicants than capacity → random assignment (b) once residents are assigned, it is permanent (no tentative acceptances, cannot let go a previously accepted student)
We keep the quota elements and the process of “accepting” vs “rejecting”
Provides the most optimal stable match in the perspective of the residents

References:
https://eprints.gla.ac.uk/107411/1/107411.pdf 
https://pmc.ncbi.nlm.nih.gov/articles/PMC8368266/