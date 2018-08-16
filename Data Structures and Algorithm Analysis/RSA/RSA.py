# 2018-8-15 ~ 2018-8-16
# https://blog.csdn.net/bian_h_f612701198412/article/details/79358771
# https://blog.csdn.net/rentenglong2012/article/details/68944518


"""
Create public and secret keys with the following procedure
    a. Two large prime numbers p and q such that p != q. The primes p and q might be, say, 1024 bites each.
    b. compute n = p * q
    c. Select a small odd integer e that is relatively prime to f(n), which f(n) = (p - 1) * (q - 1)
    d. Compute d as the mutiplicative inverse of e, modulo fn.
    e. Publish the pair P = (e, n) as the participant's RSA public key.
    f. Keep secret the pair S = (d, n) as the participant's RSA secret key.
"""


def gcd(a, b):
    """
    a = kb + r --> r = a % b
    we have:
    c = gcd(a, b)
    r = a - kb
    c|r --> c = gcd(b, r)
    gcd(a, b) = gcd(b, a % b )
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
def extendGcd(a, b):
    """
    ax + by = gcd(a, b) = d (Introduction to Algorithms P544)
    we have two case:
    a. if b == 0
        ax + 0 = gcd(a, 0) = a
        --> x = 1
            y = 0,1,... --> y = 0
    b. if a*b != 0
        then, ax + by = ax' + (a%b)y'.And a % b = a - (a/b)*b
        so, ax + by= ay' + b[x' - (a/b)y']
        --> x = x'
            y = x' - (a/b)y'
    """
    if b == 0:
        return a,1,0
    else:
        _b, _x, _y = extendGcd(b, a % b)
        d, x, y = _b, _y, _x - (a // b) * _y
        return d, x, y


def modularExponentiation(a, b, n):
    """
    See Introduction to Algorithm 560
    d = a^b(mod n)
    """
    d = 1
    b = bin(b)[2:][::-1]
    print("Binary representation of b: ", b)
    lens = len(b)
    for i in b:
        d = (d * d) % n
        if i == '1':
            d = (d * a) % n
    return d

def genKey(p, q):
    n = p * q
    fn = (p - 1) * (q - 1)
    e = 3889 
    r, d, y = extendGcd(e, fn)
    # print(r, d, y)

    #      pubkey  seckey
    return (e, n), (d, n) 

def encrypt(m, public_key):
    e = public_key[0]
    n = public_key[1]

    c = modularExponentiation(m, e, n)

    return c

def decrypt(c, secret_key):
    d = secret_key[0]
    n = secret_key[1]

    m = modularExponentiation(c, d, n)

    return m


if __name__ == "__main__":
    p = 43
    q = 59

    pubkey, seckey = genKey(p, q)

    M = 2345 # message M

    print("pubkey: ", pubkey,"\n", "seckey: ", seckey)

    C = encrypt(M, pubkey)
    D = decrypt(C, seckey)

    print(C, D)

    # End!