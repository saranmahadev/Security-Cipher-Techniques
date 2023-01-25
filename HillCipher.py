def encode(keymat, key, a, b, c):
    ret = ""
    x, y, z = 0, 0, 0
    posa = ord(a) - 65
    posb = ord(b) - 65
    posc = ord(c) - 65
    x = posa * keymat[0][0] + posb * keymat[1][0] + posc * keymat[2][0]
    y = posa * keymat[0][1] + posb * keymat[1][1] + posc * keymat[2][1]
    z = posa * keymat[0][2] + posb * keymat[1][2] + posc * keymat[2][2]
    a = key[x % 26]
    b = key[y % 26]
    c = key[z % 26]
    ret = a + b + c
    return ret

def encrypt(msg):
    keymat = [[1, 2, 1], [2, 3, 2], [2, 2, 1]]
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    enc = ""
    msg = msg.upper()
    msg = msg.replace(" ", "")
    n = len(msg) % 3
    if n != 0:
        for i in range(3 - n):
            msg += 'X'
    pdchars = list(msg)
    for i in range(0, len(msg), 3):
        enc += encode(keymat, key, pdchars[i], pdchars[i + 1], pdchars[i + 2])
    return enc

def decode(invkeymat, key, a, b, c):
    ret = ""
    x, y, z = 0, 0, 0
    posa = ord(a) - 65
    posb = ord(b) - 65
    posc = ord(c) - 65
    x = posa * invkeymat[0][0] + posb * invkeymat[1][0] + posc * invkeymat[2][0]
    y = posa * invkeymat[0][1] + posb * invkeymat[1][1] + posc * invkeymat[2][1]
    z = posa * invkeymat[0][2] + posb * invkeymat[1][2] + posc * invkeymat[2][2]
    a = key[(x % 26) if x % 26 >= 0 else (26 + x % 26)]
    b = key[(y % 26) if y % 26 >= 0 else (26 + y % 26)]
    c = key[(z % 26) if z % 26 >= 0 else (26 + z % 26)]
    ret = a + b + c
    return ret

def decrypt(enc):
    keymat = [[1, 2, 1], [2, 3, 2], [2, 2, 1]]
    key = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    dec = ""
    dechars = list(enc)
    for i in range(0, len(enc), 3):
        dec += decode(keymat, key, dechars[i], dechars[i + 1], dechars[i + 2])
    return dec

def main():
    msg = "SecurityLaboratory"
    print("simulation of Hill Cipher")
    print("-------------------------")
    print("Input message : " + msg)
    enc = encrypt(msg)
    print("encoded message : " + enc)
    dec = decrypt(enc)
    print("decoded message : " + dec)

if __name__ == "__main__":
    main()