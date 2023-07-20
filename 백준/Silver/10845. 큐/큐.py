from sys import stdin as si

class Queue:
    class _Node:
        __slots__='_elem',"_nxt"
        def __init__(self,e,n=None):
            self._elem=e; self._nxt=n
    
    def __init__(self):
        self._f=None; self._b=None; self._s=0
    def push(self,e):
        n=self._Node(e,None)
        if self.empty():
            self._f=n
        else:
            self._b._nxt=n
        self._b=n
        self._s+=1
    def pop(self):
        if self.empty():
            return -1
        else:
            e=self._f._elem
            self._f=self._f._nxt
            self._s-=1
            return e
    def size(self): return self._s
    def empty(self): return 1 if self._s==0 else 0
    def front(self): return self._f._elem if self._s!=0 else -1
    def back(self): return self._b._elem if self._s!=0 else -1
n=int(si.readline())
q=Queue()
for i in range(n):
    cmd=si.readline()[:-1]
    dc=cmd[:3]
    if dc=='pus':
        e=int(cmd[5:])
        q.push(e)
    elif dc=='pop':
        print(q.pop())
    elif dc=='siz':
        print(q.size())
    elif dc=='emp':
        print(q.empty())
    elif dc=='fro':
        print(q.front())
    else:
        print(q.back())