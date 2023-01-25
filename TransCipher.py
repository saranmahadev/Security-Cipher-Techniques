import re

def trans_cipher():
    plain_text = input("Enter the plain text: ")
    plain_text = re.sub(r'\s+', '', plain_text)
    print(plain_text)

    k = len(plain_text)
    l = 0
    col = 4
    row = k // col
    if k % col != 0:
        row += 1
    ch = [[0 for _ in range(col)] for _ in range(row)]

    for i in range(row):
        for j in range(col):
            if l < k:
                ch[i][j] = plain_text[l]
                l += 1
            else:
                ch[i][j] = '#'

    trans = [[0 for _ in range(row)] for _ in range(col)]
    for i in range(row):
        for j in range(col):
            trans[j][i] = ch[i][j]

    for i in range(col):
        for j in range(row):
            print(trans[i][j], end='')
    print()

trans_cipher()
