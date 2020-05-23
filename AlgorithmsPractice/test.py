# coding:utf-8

def test_numsEmpty():
    nums = []
    if nums:
        print("pass")
    else:
        print("fail")

def test_strOps():
    str1 = 'a'
    str2 = 'c'
    print(str2 - str1)

a = [1,2,3]
a.insert(0, -1)
print(a)