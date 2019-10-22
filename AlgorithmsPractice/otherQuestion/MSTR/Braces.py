def braces1(values):
    dicts = {'}': '{', ']': '[', ')':'('}
    stack = []
    ret = []

    for nums in values:
        stack = []
        flag = True
        for c in nums:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) == 0:
                    ret.append("NO")
                    flag = False
                    break
                else:
                    if stack[-1] != dicts[c]:
                        ret.append("NO")
                        flag = False
                        break
                    else:
                        stack.pop()
        if len(stack) == 0 and flag:
            ret.append("YES")
    
    return ret

def braces(values):
    dicts = {'}': '{', ']': '[', ')':'('}
    ret = []

    for nums in values:
        stack = []
        for c in nums:
            if c in ['(', '{', '[']:
                stack.append(c)
            else:
                if len(stack) > 0 and stack[-1] == dicts[c]:
                    stack.pop()
                else:
                    stack.append(c)
        if len(stack) == 0:
            ret.append("YES")
        else:
            ret.append("NO")
            
    
    return ret

def test():
    values = ["{}[]()","{[}]}", "}}", "}","({[]})"]
    ret = braces(values)
    print(ret)
if __name__ == '__main__':
    test()