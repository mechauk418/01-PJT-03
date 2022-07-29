import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())

for k in range(1,T+1):
    S = input()
    S = S.replace('-','') # - 문자를 '' 공백으로 치환함

    if len(S) == 16 and int(S[0]) in [3,4,5,6,9]: # 길이가 16이고 S의 시작이 3,4,5,6,9인 것을 확인
        print(f'#{k} {1}')

    else:
        print(f'#{k} {0}')



