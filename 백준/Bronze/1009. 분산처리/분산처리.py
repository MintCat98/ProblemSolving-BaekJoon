from sys import stdin
input=stdin.readline
l=[[1,5,6,0],[4,9],[2,3,7,8]]   # 반복 1/2/4개
for i in range(int(input())):
    a,b=map(int,input().split())
    a%=10
    if a in l[0]:
        print(10) if a==0 else print(a)
    elif a in l[1]:
        print((a**2)%10) if b%2==0 else print(a%10)
    else:
        print((a**4)%10) if b%4==0 else print((a**(b%4))%10)