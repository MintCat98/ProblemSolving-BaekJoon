l=iter(open(0))
next(l)
print(*sorted(map(int,l)),sep='\n')