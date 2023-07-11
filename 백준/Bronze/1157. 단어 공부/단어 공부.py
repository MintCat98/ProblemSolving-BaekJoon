# 아스키 코드 이용한 방법 by tddudwns1
s=input().upper()
m=0
for i in range(26):         # 알파벳 개수
    c=s.count(chr(i + 65))  # 대문자 알파벳은 65번부터 시작
    if m<c:
        m=c
        r=chr(i + 65)
    elif m==c:              # 만약 같은 max가 발생하면 ? 출력
        r='?'
print(r)