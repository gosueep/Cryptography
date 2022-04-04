# Misc. Mod properties


import pandas as pd
from collections import defaultdict


# mod = n
def squareMult(base, power, n):

    table = defaultdict(list)
    c = 0
    f = 1
    power = str(bin(power))[2:]

    for i in range(len(power)):

        table.update({i: [c, f, power[i], power[i:]]})

        c = c*2
        f = (f*f) % n

        if int(power[i]) == 1:
            c = c+1
            f = (f*base) % n

    table.update({'end': [c, f, '', '']})

    table = pd.DataFrame(table).transpose()
    table.columns = ['c', 'f', 'b_i', 'Bin Representation']
    print(table)
    return f


def main():
    base = int(input('Base (a): '))
    exp = int(input('Exponent: '))
    mod = int(input('Mod: '))
    print(squareMult(base, exp, mod))


if __name__ == "__main__":
    main()
