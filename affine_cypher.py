'''
    Script used in the resolution of the exercicies 4 to 6, 8, 9, 12(a) of the discipline 
    GB-122 Cryptography. 
    Book: Applied Abstract Algebra with MapleTM and MATLAB - Third edition - Chapter 6
'''

def create_dict():
    return ({chr(y):y-65 for y in range(65,91)})

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

def encrypt(dic, text, shift, a, b):
    ct = []
    keys = [dic[i] for i in list(text)]
    keys = [(keys[i] * a + shift) % 26 for i in range(len(keys))]
        
    for i in keys:
        for k, v in dic.items():
            if v == i:
                ct.append(k)
    return ''.join(ct)

def decrypt(dic, text, shift, a, b):
    pt = []
    keys = [dic[i] for i in list(text)]
    
    if gcd(a,b) == 1:
        keys = [(bezout_identity(a,b) * (keys[i] - shift) % b) for i in range(len(keys))]
        for i in keys:
            for k, v in dic.items():
                if v == i:
                    pt.append(k)
        return ''.join(pt)
    else: 
        print("Impossible to decrypt")

if __name__ == "__main__":
    plaintxt = ''
    cyphertxt = ''
    a, b = 25, 26
    shift = 3
    
    dic = create_dict()
    cyphertxt = encrypt(dic, plaintxt.replace(" ",""), shift, a, b)
    print(cyphertxt)
    cyphertxt = encrypt(dic, cyphertxt, shift, a, b)
    print(cyphertxt)
    
    '''
        [-- BRUTE FORCE MODE --]
    '''
    # for i in range(b):
    #     if gcd(i,b) == 1:
    #         for j in range(b):
    #             plaintxt = decrypt(dic,cyphertxt, j, i, b)
    #             print(i, j, plaintxt)  
