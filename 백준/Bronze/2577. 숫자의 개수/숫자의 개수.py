# 이렇게 심플하게 풀 수 있다니..
n=int(input())*int(input())*int(input())
for i in range(10):
    print(str(n).count(str(i)))