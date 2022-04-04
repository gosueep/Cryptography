# Finds primitive roots of n
# Assumes n is prime

# Finds by testing all numbers a where a^(n-1) mod n = 1
# If all powers from 2 to n-2 are not 1, is a primitive root

import pandas as pd
from collections import defaultdict


# Normal Primitive Root Check
def primRoots(n):
    roots = []
    for a in range(1, n):
        if checkPrimRoot(a, n):
            roots.append(a)
    return roots


def checkPrimRoot(a, n):
    # Euler's totient theorem, assuming n is prime
    phi = n - 1
    # Check no powers other than the first and last (n-1) are 1
    for power in range(2, n-2):
        if (a ** power) % n == 1:
            return False

    return True


# Verbose primitive roots - Prints out intermediate results
def primRoots_table(n):
    roots = defaultdict(list)
    for a in range(1, n):
        row = []
        for power in range(1, n):
            row.append((a ** power) % n)
        roots.update({a: row})

    roots = pd.DataFrame(roots)
    roots.index += 1
    roots = roots.transpose()
    roots.columns = ["a" + str(x) for x in range(1, n)]
    return roots


def main():
    n = int(input("Find primitive roots of: "))
    print(primRoots(n))
    print(primRoots_table(n))


if __name__ == "__main__":
    main()
