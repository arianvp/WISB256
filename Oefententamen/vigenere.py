coded = input()
password = input()

def toNum(x):
    return ord(x) - ord('a')

def toChar(x):
    return chr(x + ord('a'))


def decrypt(msg,password):
    res = ""
    for i,c in enumerate(msg):
        c2 = (toNum(c) - toNum(password[i % len(password)])) % 26
        res = res + (toChar(c2))
    return res

print(decrypt(coded,password))





