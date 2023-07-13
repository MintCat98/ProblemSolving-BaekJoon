l=[int(input()) for i in range(10)]
s={l[i]%42 for i in range(10)}
print(len(s))