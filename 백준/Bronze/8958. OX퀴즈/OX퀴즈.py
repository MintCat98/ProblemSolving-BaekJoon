n=int(input())
for i in range(n):
    a=input()
    j=0; c=0; s=0
    while True:
        try:
            while a[j]=='O':
                j+=1; c+=1; s+=c
            while a[j]=='X':
                j+=1; c=0
        except: break
    print(s)