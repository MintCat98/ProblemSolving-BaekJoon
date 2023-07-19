from sys import stdin as si
while True:
    n=si.readline().strip('\n')
    if n=='0': break
    l=len(n); h=int(l/2)
    print('yes') if n==n[::-1] else print('no')