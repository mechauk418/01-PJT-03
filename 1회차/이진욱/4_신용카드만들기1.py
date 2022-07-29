import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())

for k in range(1,T+1):
    N_list = list(map(int,input().split()))

    odd = sum ( [ 2 * N_list[i] for i in range(len(N_list)) if i % 2 == 0 ]   ) # 홀수번째 숫자의 두배를 더한 값의 합

    even = sum ( [ N_list[i] for i in range(len(N_list)) if i % 2 == 1 ]   ) # 짝수번째 숫자의 총합

    if (odd+even) % 10 == 0:
        print(f'#{k} {0}')
    else:
        ans = 10- ((odd + even) % 10)
        print(f'#{k} {ans}')