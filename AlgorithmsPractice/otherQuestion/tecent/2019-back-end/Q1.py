import sys
"""
HG[3|B[2|CA]]F

HGBCACABCACABCACAF
"""
def solver(s):
    ret = [""]
    digit = 0
    number = []
    for i, c in enumerate(s):
        if c.isdigit():
            digit = digit* 10 + int(c)
        elif c == '[':
            ret.append("")
        elif c == ']':
            d = number.pop()
            last = ret.pop()
            ret[-1] += last*d 
        elif c == '|':
            number.append(digit)
            digit = 0
        else:
            ret[-1] += c 

    return ret[0] 

def test():
    s = "HG[3|B[2|CA]]F"
    e = "HGBCACABCACABCACAF"
    ret = solver(s)
    print(ret == e)

if __name__ == '__main__':
    test()


