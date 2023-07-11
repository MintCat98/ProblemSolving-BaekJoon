import sys
l=[]
while True:
    try: l.append(int(sys.stdin.readline()))
    except: break
m=max(l)
print(m)
print(l.index(m)+1)