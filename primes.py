from math import floor, ceil, sqrt


def primeFactors(num):
    pfacts = set()
    for i in range(2, int(num/2)):
        if num % i == 0:
            pfacts.add(i)
    pfacts = list(pfacts)
    pfacts.sort()
    return pfacts


def isPrime(num):
    if num % 2 == 0:
        return False
    for i in range(3, ceil(sqrt(num))+2, 2):
        if num % i == 0:
            return False
    return True


def totient(num):
    if isPrime(num):
        return num-1

    pfacts = primeFactors(num)
    if len(pfacts) == 2:
        return (pfacts[0]-1) * (pfacts[1]-1)


def main():
    num = int(input("Prime factors of: "))
    print("Prime? " + str(isPrime(num)))
    print(f'Prime Factors: {primeFactors(num)}')
    print(f'Totient: {totient(num)}')




if __name__ == "__main__":
    main()