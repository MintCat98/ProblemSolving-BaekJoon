import sys
a=int(sys.stdin.readline())
if a<60:
    print('F')
elif 59<a<70:
    print('D')
elif 69<a<80:
    print('C')
elif 79<a<90:
    print('B')
else:
    print('A')