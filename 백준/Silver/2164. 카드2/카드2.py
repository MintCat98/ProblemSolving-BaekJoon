class Queue:
    class _Node:
        __slots__='_elem',"_nxt"
        def __init__(self,e,n=None):
            self._elem=e; self._nxt=n
    def __init__(self):
        self._f=None; self._b=None; self._s=0
    def enq(self,e):
        n=self._Node(e,None)
        if self._s==0:
            self._f=n
        else:
            self._b._nxt=n
        self._b=n
        self._s+=1
    def deq(self):
        e=self._f._elem
        self._f=self._f._nxt
        self._s-=1
        return e
    def size(self): return self._s
    def head(self): return self._f._elem
n=int(input())
q=Queue()
for i in range(1,n+1):
    q.enq(i)
i=1
while q.size()!=1:
    if i%2!=0: q.deq()
    else: q.enq(q.head()); q.deq()
    i+=1
print(q.head())