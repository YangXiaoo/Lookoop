# coding:utf-8
# 2019-2-1

# 66. Python的生成器
def foo(arg=None):
    print("start foo.")
    try:
        while True:
            try:
                arg = yield arg # 第二次调用的时候会返回 None
            except Exception as e:
                print(str(e))
    finally:
        print("end foo")

g = foo(1)
print(g.__next__())
print(g.send(2))
print(g.close())