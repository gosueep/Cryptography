import hashlib
import random
import binascii

LENGTH = 6                              # length of hex digest (24 bits)
charset = "0123456789abcdef"            # all hex values


def oneway(filename):
    file = open(filename, 'rb')  # open file
    h = hashlib.sha256(file.read())  # get hash of input file
    original = h.hexdigest()[:6]  # take first 24 bits of hash (first 6 chars of hex digest)

    # print truncated hash
    print(f'Original Hash of file (truncated to 24 bits): {original}')

    # try random strings until finding the hash
    randHash = ""
    iterations = 0
    while randHash != original:
        randHash = ''.join(random.choice(charset) for i in range(6))
        iterations += 1

    print(iterations)


def collision():
    # try random strings to hash until finding a collision hash
    randString1 = ""
    randString2 = "not equal"
    randHash1 = ""
    randHash2 = "not equal"
    iterations = 0
    while randHash1 != randHash2 and randString1 != randString2:
        randString1 = ''.join(random.choice(charset) for i in range(6))
        randHash1 = hashlib.sha256(bytes(randString1, 'utf8')).hexdigest()[:6]

        randString2 = ''.join(random.choice(charset) for i in range(6))
        randHash2 = hashlib.sha256(bytes(randString2, 'utf8')).hexdigest()[:6]

        iterations += 1
        # print(iterations)

    # print iterations it took to find it
    print(randHash1)
    print(randHash2)
    print(iterations)


def bitdiff(hash1, hash2):

    if len(hash1) != len(hash2):
        print("NOT SAME LENGTH")
        return False

    hash1 = bin(int(hash1, 16))[2:]
    hash2 = bin(int(hash2, 16))[2:]

    length = len(hash1)
    sameBits = 0
    for byte in range(length):
        if hash1[byte] == hash2[byte]:
            sameBits += 1

    print(f'{sameBits} out of the {length} bits are the same')


if __name__ == "__main__":
    oneway('input.txt')

    for trials in range(3):
        collision()


    bitdiff("f3663e631ec1d5371fc155c6635fe8dc",
            "108b3f210feef0734dc229fbdde5b867")
    bitdiff("e9ff8242b5ad31a0f77a70e19539f2b27c304724f1f0c51b9d7aa0ed9f590112",
            "dc7526d645d44c1bbc9fc2c333e96b400ee455d6286ee7f4ed07e37b616b1d77")
