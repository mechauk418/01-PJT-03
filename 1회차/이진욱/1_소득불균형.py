import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())

for i in range(T):
    N = int(input())

    income_list = list(map(int,input().split())) 

    income_avg = sum(income_list) / len(income_list) # 소득의 평균을 구함

    ans = len([ i for i in income_list if i <= income_avg  ]) # 소득 리스트에서 그 값이 평균보다 낮은 값들로 구성된 리스트의 길이를 구함

    print(f'#{i+1} {ans}' )

