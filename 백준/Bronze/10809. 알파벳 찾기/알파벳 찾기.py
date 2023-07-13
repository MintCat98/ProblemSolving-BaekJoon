s=input()
l=[]
for i in range(26):
    l.append(s.find(chr(i+97)))
print(' '.join(map(str,l)))