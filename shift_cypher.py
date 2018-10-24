'''
    Script used in the resolution of the exercicies 1 to 3 of the discipline GB-122 Cryptography. 
    Book: Applied Abstract Algebra with MapleTM and MATLAB - Third edition - Chapter 6
'''

def create_dict():
    return ({chr(y):y-65 for y in range(65,91)})

def encrypt(dic, text, shift):
    ct = []
    keys = [dic[i] for i in list(text)]
    keys = [(keys[i] + shift) % 26 for i in range(len(keys))]

    for i in keys:
        for k, v in dic.items():
            if v == i:
                ct.append(k)
    return ''.join(ct)

def decrypt(dic, text, shift):
    pt = []
    keys = [dic[i] for i in list(text)]
    keys = [(keys[i] - shift) % 26 for i in range(len(keys))]
    
    for i in keys:
        for k, v in dic.items():
            if v == i:
                pt.append(k)
    return ''.join(pt)

if __name__ == "__main__":
    # Insert the plaintext or cyphertxt
    plaintxt = 'SEND TARGET'
    cyphertxt = ''
    shift = 3

    dic = create_dict()
    cyphertxt = encrypt(dic, plaintxt.replace(" ",""), shift)
    print(cyphertxt)
    plaintxt = decrypt(dic, cyphertxt, shift)
    print(plaintxt)

    '''
        [-- BRUTE FORCE MODE --]
    '''
    # cyphertxt = 'DOHKCDGYCDOZ'
    # for i in range(0,25):
    #     plaintxt = decrypt(dic, cyphertxt, i)
    #     print(plaintxt)    
