from sys import stdin as si
while True:
    n=si.readline().strip('\n')
    if n=='0': break
    nr=n[::-1]
    l=len(n); h=int(l/2)
    if l%2==0:
        print('yes') if n[:h]==nr[:h] else print('no')
    else:
        print('yes') if n[:h]==nr[:h] else print('no')