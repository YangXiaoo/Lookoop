#OS模块遍历文件
#date(2018-4-15)
import os

dirpath = input("请输入要遍历的文件夹:")

def getdir(dirpath,level=0):
        level += 2
        if not dirpath:
                dirpath = os.getcwd()
        mylist = os.listdir(dirpath) #写到if条件外面
        for name in mylist:
                print('-'*level+'|'+name)
                name = os.path.join(dirpath,name)
                if os.path.isdir(name):
                        getdir(name,level)

getdir(dirpath)



#捕获异常
def func(var, index):
	return var[index]

mylist = input('请输入你要访问的列表：')
index = input('请输入你要访问的位置：')

try:
	#input获得的是字符串，需要转为列表
	mylist = eval(mylist)
	index = int(index)
	num = func(mylist, index)
except TypeError:
	print('你的传递顺序颠倒了')
except IndexError:
	print('你的索引超出了列表上限')
except ValueError:
	print('值出现错误')
else:
	print(num)
finally:
	print('使用完毕')

	