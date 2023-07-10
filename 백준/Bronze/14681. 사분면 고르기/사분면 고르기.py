import sys
x=int(sys.stdin.readline())
y=int(sys.stdin.readline())
if x>0:
    print(1) if y>0 else print(4)
else:
    print(2) if y>0 else print(3)