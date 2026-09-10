def print_acc_rej(hospital, accepted, rejected):
    print(f"'h{hospital + 1}': Accepted: ", end="")
    print_app(accepted, end=" ")
    print(f"Rejected: ", end="")
    print_app(rejected, end="\n")

def print_A(A):
    print("{", end="")
    for resident, hospital in enumerate(A):
        print(f"'r{resident}': ", end="")
        if hospital: print(f"'h{hospital + 1}', ", end="")
    print("}")

def print_H(H):
    print("{", end="")
    for hospital, applicants in enumerate(H):
        print(f"'h{hospital + 1}': ", end="")
        print_app(applicants)
        print(", ", end="")
    print("}")

def print_C(C):
    print("{", end="")
    for hospital, capacity in enumerate(C):
        print(f"'h{hospital + 1}': {capacity}, ", end="")
    print("}")

def print_hosp(h_s):
    print(f"{[f'h{h + 1}' for h in h_s]}", end="")

def print_app(r_s, end="false"):
    print(f"{[f'r{r}' for r in r_s]}", end="")
    if end != "false":
        print(end, end="")
