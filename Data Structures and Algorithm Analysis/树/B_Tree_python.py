from random import randint,choice
from bisect import bisect_left
from collections import deque
class InitError(Exception):
    pass
class ParaError(Exception):
    pass
class KeyValue(object):
    __slots__=('key','value')
    def __init__(self,key,value):
        self.key=key
        self.value=value
    def __str__(self):
        return str((self.key,self.value))
    def __cmp__(self,key):
        if self.key>key:
            return 1
        elif self.key==key:
            return 0
        else:
            return -1
class BtreeNode(object):
    def __init__(self,t,parent=None):
        if not isinstance(t,int):
            raise InitError('degree of Btree must be int type')
        if t<2:
            raise InitError('degree of Btree must be equal or greater then 2')
        else:
            self.klist=[]
            self.clist=[]
            self.parent=parent
            self.__degree=t
    @property
    def degree(self):
        return self.__degree
    def isleaf(self):
        return len(self.clist)==0

    def traversal(self):
        result=[]
        def get_value(n):
            if n.clist==[]:
                result.extend(n.klist)
            else:
                for i,v in enumerate(n.klist):
                    get_value(n.clist[i])
                    result.append(v)
                get_value(n.clist[-1])
        get_value(self)
        return result

    def show(self):
        q=deque()
        h=0
        q.append([self,h])
        while True:
            try:
                w,hei=q.popleft()
            except IndexError:
                return
            else:
                print ([v for v in w.klist],'the height is',hei)
                if w.clist==[]:
                    continue
                else:
                    if hei==h:
                        h+=1
                    q.extend([[v,h] for v in w.clist])

    def getmax(self):
        n=self
        while not n.isleaf():
            n=n.clist[-1]
        return (n.klist[-1],n)

    def getmin(self):
        n=self
        while not n.isleaf():
            n=n.clist[0]
        return (n.klist[0],n)

class IndexFile(object):
    def __init__(fname,cellsize):
        f=open(fname,'wb')
        f.close()
        self.name=fname
        self.cellsize=cellsize
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    def write_obj(obj,pos):
           pass
    def read_obj(obj,pos):
        pass
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
class Btree(object):
    def __init__(self,t):
        self.__degree=t
        self.__root=BtreeNode(t)
    @property
    def degree(self):
        return self.__degree
    def traversal(self):
        """
        use dfs to search a btree's node
        """
        return self.__root.traversal()
    def show(self):
        """
        use bfs to show a btree's node and its height
        """
        return self.__root.show()
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
    def search(self,mi=None,ma=None):
        """
        search key-value pair within range mi<=key<=ma.
        if mi or ma is not specified,the searching range
        is key>=mi or key <=ma
        """
        result=[]
        node=self.__root
        if mi is None and ma is None:
            raise ParaError('you need setup searching range')
        elif mi is not None and ma is not None and mi>ma:
            raise ParaError('upper bound must be greater or equal than lower bound')
        def search_node(n):
            if mi is None:
                if not n.isleaf():
                    for i,v in enumerate(n.klist):
                        if v<=ma:
                            result.extend(n.clist[i].traversal())
                            result.append(v)
                        else:
                            break
                    search_node(n.clist[-1])
                else:
                    for v in n.klist:
                        if v<=ma:
                            result.append(v)
                        else:
                            break
            elif ma is None:
                if not n.isleaf():
                    for i,v in enumerate(n.klist):
                        if v<mi:
                            continue
                        else:
                            search_node(n.clist[i])
                            while i<len(n.klist):
                                result.append(n.klist[i])
                                result.extend(n.clist[i+1].traversal())
                                i+=1
                            break
                    if v.key<mi:
                        search_node(n.clist[-1])
                else:
                    for v in n.klist:
                        if v>=mi:
                            result.append(v)
            else:
                if not n.isleaf():
                    for i,v in enumerate(n.klist):
                        if v<mi:
                            continue
                        elif mi<=v<=ma:
                            search_node(n.clist[i])
                            result.append(v)
                        elif v>ma:
                            search_node(n.clist[i])
                    if v<=ma:
                        search_node(n.clist[-1])
                else:
                    for v in n.klist:
                        if mi<=v<=ma:
                            result.append(v)
                        elif v>ma:
                            break
        search_node(node)
        return result
    def insert(self,key_value):
        node=self.__root
        full=self.degree*2-1
        mid=int(full/2+1)
        print("insert: ", key_value)
        def split(n):
            new_node=BtreeNode(self.degree,parent=n.parent)
            new_node.klist=n.klist[mid:]
            new_node.clist=n.clist[mid:]
            for c in new_node.clist:
                c.parent=new_node
            if n.parent is None:
                newroot=BtreeNode(self.degree)
                newroot.klist=[n.klist[mid-1]]
                newroot.clist=[n,new_node]
                n.parent=new_node.parent=newroot
                self.__root=newroot
            else:
                i=n.parent.clist.index(n)
                n.parent.klist.insert(i,n.klist[mid-1])
                n.parent.clist.insert(i+1,new_node)
            n.klist=n.klist[:mid-1]
            n.clist=n.clist[:mid]
            return n.parent
        def insert_node(n):
            if len(n.klist)==full:
                insert_node(split(n))
            else:
                if n.klist==[]:
                    n.klist.append(key_value)
                else:
                    if n.isleaf():
                        p=bisect_left(n.klist,key_value)  #locate insert point in ordered list klist
                        n.klist.insert(p,key_value)
                    else:
                        p=bisect_left(n.klist,key_value)
                        insert_node(n.clist[p])
        insert_node(node)

    def delete(self,key_value):
        node=self.__root
        mini=self.degree-1
        def merge(n,i):
            n.clist[i].klist=n.clist[i].klist+[n.klist[i]]+n.clist[i+1].klist
            n.clist[i].clist=n.clist[i].clist+n.clist[i+1].clist
            n.clist.remove(n.clist[i+1])
            n.klist.remove(n.klist[i])
            if n.klist==[]:
                n.clist[0].parent=None
                self.__root=n.clist[0]
                del n
                return self.__root
            else:
                return n
        def tran_l2r(n,i):
            left_max,left_node=n.clist[i].getmax()
            right_min,right_node=n.clist[i+1].getmin()
            right_node.klist.insert(0,n.klist[i])
            del_node(n.clist[i],left_max)
            n.klist[i]=left_max
        def tran_r2l(n,i):
            left_max,left_node=n.clist[i].getmax()
            right_min,right_node=n.clist[i+1].getmin()
            left_node.klist.append(n.klist[i])
            del_node(n.clist[i+1],right_min)
            n.klist[i]=right_min
        def del_node(n,kv):
            p=bisect_left(n.klist,kv)
            if not n.isleaf():
                if p==len(n.klist): # kv > max(n.klist)
                    if len(n.clist[-1])>mini:
                        del_node(n.clise[p],kv)
                    elif len(n.clist[p-1])>mini:
                        tran_l2r(n,p-1)
                        del_node(n.clist[-1],kv)
                    else:
                        del_node(merge(n,p-1),kv)
                else:
                    if n.klist[p]==kv:
                        left_max,left_node=n.clist[i].getmax()
                        if len(n.clist[p].klist)>mini:
                            del_node(n.clist[p],left_max)
                            n.klist[p]=left_max
                        else:
                            right_min,right_node=n.clist[i+1].getmin()
                            if len(n.clist[p+1].klist)>mini:
                                del_node(n.clist[p+1],right_min)
                                n.klist[p]=right_min
                            else:
                                del_node(merge(n,p),kv)
                    else:
                        if len(n.clist[p].klist)>mini:
                            del_node(n.clist[p],kv)
                        elif len(n.clist[p+1].klist)>mini:
                            tran_r2l(n,p)
                            del_node(n.clist[p],kv)
                        else:
                            del_node(merge(n,p),kv)
            else:
                try:
                    pp=n.klist[p]
                except IndexError:
                    return -1
                else:
                    if pp!=kv:
                        return -1
                    else:
                        n.klist.remove(kv)
                        return 0
        del_node(node,key_value)
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
def test():
    mini=50
    maxi=200
    testlist=[]
    for i in range(1,1001):
        key=randint(1,1000)
        #key=i
        value=4
        testlist.append(key)
    mybtree=Btree(5)
    for x in testlist:
        # print(x)
        mybtree.insert(x)
    print ('my btree is:\n')
    mybtree.show()
    #mybtree.delete(testlist[0])
    #print '\n the newtree is:\n'
    #mybtree.show()
    print ('\nnow we are searching item between %d and %d\n\n'%(mini,maxi))
    print ([v for v in mybtree.search(mini,maxi)])
    #for x in mybtree.traversal():
    #    print x
if __name__=='__main__':
    test()