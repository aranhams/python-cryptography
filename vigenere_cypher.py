def create_dict():
    return ({chr(y):y-65 for y in range(65,91)})

def encrypt(_plaintxt=None, _key=None, _b=26, _dict=create_dict()):
    ct = [] 
    plaintxt = [_dict[i] for i in list(_plaintxt)]
    key = [_dict[i] for i in list(_key)]
    cyphertxt = [(plaintxt[i]+key[i%len(key)])%_b for i in range(len(plaintxt))]

    for i in cyphertxt:
        for k, v in _dict.items():
            if v == i:
                ct.append(k)
    return ''.join(ct)

def decrypt(_cyphertxt=None, _key=None, _b=26, _dict=create_dict()):
    pt = [] 
    cyphertxt = [_dict[i] for i in list(_cyphertxt)]
    key = [_dict[i] for i in list(_key)]
    plaintxt = [(cyphertxt[i]-key[i%len(key)])%_b for i in range(len(cyphertxt))]

    for i in plaintxt:
        for k, v in _dict.items():
            if v == i:
                pt.append(k)
    return ''.join(pt)

if __name__ == '__main__':
    plaintxt = 'JOIN THE PARTY'
    key = 'ABOUT'

    cyphertxt = encrypt(plaintxt.replace(" ",""), key)
    print(cyphertxt)
    plaintxt = decrypt(cyphertxt, key)
    print(plaintxt)
