from sys import stdin as si

def pm(l):
    s=[]
    for c in l:
        if c in "([": s.append(c)
        elif c=="]":
            if len(s)==0:
                return "no"
            if s[-1]=="[":
                s.pop()
            else: return "no"
        else: # ")"
            if len(s)==0:
                return "no"
            if s[-1]=="(":
                s.pop()
            else: return "no"
    if len(s)==0:
        return "yes"
    else: return "no"

l=si.readlines()[:-1]
ps="()[]"
for i in range(len(l)):
    f=[]    # ps filter
    for c in l[i]:
        if c in ps: f.append(c)
    # if empty -> yes
    if len(f)==0:
        print("yes")
        continue
    # start with close
    if f[0] in ")]":
        print("no")
        continue
    # cases
    print(pm(f))