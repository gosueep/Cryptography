
def gcd(a, b):
    print(a)
    if b == 0 : return 1
    else : return gcd(b, a % b)

def main():
    print(gcd(24140, 40902))
    #gcd(1234, 4321)


if __name__ == "__main__":
    main()