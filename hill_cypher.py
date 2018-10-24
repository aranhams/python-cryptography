'''
    Script used in the resolution of the exercicies in the discipline GB-122 Cryptography. 
    Book: Applied Abstract Algebra with MapleTM and MATLAB - Third edition - Chapter 6
'''

import numpy as np
import math

def gcd(a, b):
    while b != 0:
        (a, b) = (b, a % b)
    return a

def bezout_identity(a, b):
    r = a
    r_prime = b
    u = v_prime = 1
    v = u_prime = 0

    while(r_prime != 0):
        q = int(r/r_prime)
        rs = r; us = u; vs = v
        r = r_prime; u = u_prime; v = v_prime
        r_prime = rs - q * r
        u_prime = us - q * u_prime
        v_prime = vs - q * v_prime
    
    return u

def inv_matrix(matrix,b):
    return bezout_identity(int(np.linalg.det(matrix)),b) * (np.linalg.inv(matrix) * np.linalg.det(matrix))

def create_dict():
    return ({chr(y):y-65 for y in range(65,91)})

def encrypt(dic, text, m, b = 0):
    ct = []
    msgmatrix = []
   
    keys = [dic[i] for i in list(text)]
    msgmatrix = np.matrix(keys).round().reshape((int(len(keys)/len(m)), len(m)))
    keys = [x for x in np.array((msgmatrix * m ) % b).flat]
    
    for i in keys:
        for k, v in dic.items():
            if v == i:
                ct.append(k)
    return ''.join(ct)

   
def decrypt(dic, text, m, b = 0):
    pt = []
    msgmatrix = []

    keys = [dic[i] for i in list(text)]
    if gcd(int(np.linalg.det(m)),b) == 1:
        try: 
            msgmatrix = np.matrix(keys).round().reshape((int(len(keys)/len(m)), len(m)))
        except ValueError:
            pass
        keys = [x for x in np.array((msgmatrix * inv_matrix(m,b)) % b).flat]
        keys = [round(keys[i],0) % b for i in range(len(keys)) ]
        for i in keys:
            for k, v in dic.items():
                if v == i:
                    pt.append(k)
        return ''.join(pt)

if __name__ == "__main__":
    m1 = [[13, 7], [8, 21]]
    m2 = [[1, 2, 1], 
          [3, 1, 0], 
          [0, 2, 1]]
    plaintxt1 = 'SEND TARGET STATUS'
    plaintxt2 = 'BULL DURHAM AA'
    cyphertxt = 'FLBIPURCRGAO'
    

    dic = create_dict()
    cyphertxt = encrypt(dic, plaintxt2.replace(" ",""), m2, 26)
    print(cyphertxt)
    plaintxt = decrypt(dic, cyphertxt, m2, 26)
    print(plaintxt)

    '''
        [-- BRUTE FORCE MODE --]
    '''
    # for i in range(26):
    #     for j in range(26):
    #         for k in range(26):
    #             for l in range(26):                 
    #                 M = [[i,j],[k,l]]
    #                 plaintxt = decrypt(dic,cyphertxt,M,26)
    #                 if plaintxt != None:
    #                     print(plaintxt)
    # cyphertxt = 'DOHKCDGYCDOZ'
    # for i in range(0,25):
    #     plaintxt = decrypt(dic,cyphertxt,i)
    #     print(plaintxt)



    
