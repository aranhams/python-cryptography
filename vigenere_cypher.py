def createdict_():
    return ({chr(y):y-65 for y in range(65,91)})

def encrypt(plaintxt_=None, key_=None, b_=26, dict_=createdict_()):
    ct = [] 
    plaintxt = [dict_[i] for i in list(plaintxt_)]
    key = [dict_[i] for i in list(key_)]
    cyphertxt = [(plaintxt[i]+key[i%len(key)])%b_ for i in range(len(plaintxt))]

    for i in cyphertxt:
        for k, v in dict_.items():
            if v == i:
                ct.append(k)
    return ''.join(ct)

def decrypt(cyphertxt_=None, key_=None, b_=26, dict_=createdict_()):
    pt = [] 
    cyphertxt = [dict_[i] for i in list(cyphertxt_)]
    key = [dict_[i] for i in list(key_)]
    plaintxt = [(cyphertxt[i]-key[i%len(key)])%b_ for i in range(len(cyphertxt))]

    for i in plaintxt:
        for k, v in dict_.items():
            if v == i:
                pt.append(k)
    return ''.join(pt)

if __name__ == '__main__':
    plaintxt = 'CRYPTOGRAPHY'
    key = 'LNCC'

    cyphertxt = encrypt(plaintxt.replace(" ",""), key)
    print(cyphertxt)
    plaintxt = decrypt(cyphertxt, key)
    print(plaintxt)
