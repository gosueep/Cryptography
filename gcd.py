def gcd(a, b):
    if b == 0:
        return 1
    else:
        return gcd(b, a % b)


def euclid(a, b):
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = euclid(b % a, a)
        return g, x - (b // a) * y, y


# Modular Inverse of a mod Z (mod)
def inverse(a, z):
    g, x, y = euclid(a, z)
    if g != 1:
        print(f"Modular inverse of {a} in Z_{z} doesn't exist")
    else:
        return euclid(a, z)[1] % z


def main():
    print(inverse(59, 71))


if __name__ == "__main__":
    main()
