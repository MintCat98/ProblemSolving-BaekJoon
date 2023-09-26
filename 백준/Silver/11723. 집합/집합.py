from sys import stdin
input=stdin.readline
s=set()
for _ in range(int(input())):
    cmd=input()[:-1]
    if cmd!='all' and cmd!='empty':
        cmd,num=cmd.split(); num=int(num)
    if cmd=='add':
        s.add(num)
    elif cmd=='remove':
        if len(s)!=0:
            s.remove(num)
    elif cmd=='check':
        print(1) if num in s else print(0)
    elif cmd=='toggle':
        s.remove(num) if num in s else s.add(num)
    elif cmd=='all':
        s={n for n in range(1,21)}
    else: s=set()