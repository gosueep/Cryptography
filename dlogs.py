# Finds Discrete logarithms

import pandas as pd
from primitiveRoots import primRoots, primRoots_table, checkPrimRoot


# i = dlog_(a,p) b
# b = a^i mod p
# finds i
def dlog(b, a, p):

    if not checkPrimRoot(a, p):
        print('WARNING: ANSWER EITHER DOES NOT EXIST OR IS NOT UNIQUE')
        return -1

    i = 0
    while (a**i) % p != b:
        print(f'{a}^{i} mod p = {(a**i) % p}')
        i += 1
    print(f'{a}^{i} mod p = {(a ** i) % p}')
    return i


def main():
    print("Discrete Log")
    b = int(input('Num/Base: '))
    a = int(input('a: '))
    p = int(input('p: '))
    print(f'dlog: {dlog(b, a, p)}')

    # Check with table
    # rootTable = primRoots_table(p)
    # rootList = rootTable.iloc[a-1]
    # print(rootList[rootList == b])


if __name__ == "__main__":
    main()
