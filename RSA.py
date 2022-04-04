# RSA Encryption / Decryption

from gcd import gcd, euclid, inverse


class RSA:

    def __init__(self, p, q, e):
        self.p = p
        self.q = q
        self.n = p*q
        self.e = e
        self.PU = {e, self.n}
        self.totient = (p-1) * (q-1)
        self.d = inverse(e, self.totient)
        print(f'Public Key: {self.PU}')
        print(f'Private Key: {self.d}')

    def encrypt(self, M):
        C = (M ** self.e) % self.n
        return C


    def rsa_decrypt(self, C):
        M = (C ** self.d) % self.n
        return M


def main():
    # p = int(input("p: "))
    # q = int(input("q: "))
    # e = int(input("e: "))
    # M = int(input("M: "))

    p = 7
    q = 11
    e = 17
    M = 8

    rsa = RSA(p, q, e)

    print(f'Original message: {M}')
    # print(f'phi: {rsa.totient}')

    C = rsa.encrypt(M)
    print(f'Ciphertext: {C}')
    print(f'Decrypted: {rsa.rsa_decrypt(C)}')


if __name__ == "__main__":
    main()