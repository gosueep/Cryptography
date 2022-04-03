#from pandas import *

import numpy as np


def AES(ptext, key):
    AES_Round(ptext, key)

def AES_Round(ptext, key):
    ptext = initialState(ptext)
    print(ptext)


def initialState(ptext):
    initStateMatrix = []
    for i in range(0, len(ptext), 8):
        row = []
        rowOut = ""
        for j in range(i, i+8, 2):
            byte = str(ptext[j:j+2])
            row.append(byte)
            rowOut += byte + " "
        initStateMatrix.append(row)
        print(rowOut)

    return np.transpose(initStateMatrix)


#def AddRoundKey():

#def SubBytes():

#def ShiftRows():

#def MixCols():


def main():
    ptext = "000102030405060708090A0B0C0D0E0F"
    key = "01010101010101010101010101010101"
    AES(ptext, key)

if __name__ == "__main__" :
    main()