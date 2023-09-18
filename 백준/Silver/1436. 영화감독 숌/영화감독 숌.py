n=int(input())
doom='666'
t=665; c=0  # title, counter
while c!=n:
    t+=1
    if doom in str(t):
        c+=1
print(t)