from sys import stdin as si

class Deque:
    class _Node:
        __slots__='_elem','_bfr','_nxt'
        def __init__(self,e,b=None,n=None):
            self._elem=e; self._bfr=b; self._nxt=n
    
    def __init__(self):
        self._f=None; self._b=None; self._s=0
    def push_f(self,e):
        n=self._Node(e,None)
        if self.empty():
            self._f=n; self._b=n
        else:
            self._f._bfr=n
            n._nxt=self._f
        self._f=n
        self._s+=1
    def push_b(self,e):
        n=self._Node(e,None)
        if self.empty():
            self._f=n; self._b=n
        else:
            self._b._nxt=n
            n._bfr=self._b
        self._b=n
        self._s+=1
    def pop_f(self):
        if self.empty():
            return -1
        else:
            e=self._f._elem
            self._f=self._f._nxt
            if self._s!=1:
                self._f._bfr=None
            self._s-=1
            return e
    def pop_b(self):
        if self.empty():
            return -1
        else:
            e=self._b._elem
            self._b=self._b._bfr
            if self._s!=1:
                self._b._nxt=None
            self._s-=1
            return e
    def size(self): return self._s
    def empty(self): return 1 if self._s==0 else 0
    def front(self): return self._f._elem if self._s!=0 else -1
    def back(self): return self._b._elem if self._s!=0 else -1

n=int(si.readline())
d=Deque()
for i in range(n):
    cmd=si.readline()[:-1]
    dc=cmd[:3]
    if dc=='pus':
        d.push_f(int(cmd[11:])) if cmd[5]=='f' else d.push_b(int(cmd[10:]))
    elif dc=='pop':
        print(d.pop_f()) if cmd[4]=='f' else print(d.pop_b())
    elif dc=='siz':
        print(d.size())
    elif dc=='emp':
        print(d.empty())
    elif dc=='fro':
        print(d.front())
    else:
        print(d.back())