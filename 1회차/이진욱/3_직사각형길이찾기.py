import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())

for k in range(1,T+1):
    N_list = list(map(int,input().split()))
    ans = 0

    for i in range(3):
        if N_list.count(N_list[i]) == 1 or N_list.count(N_list[i]) == 3:
            # 주어진 3개의 숫자중에서 리스트에 1개있거나 3개있는 숫자를 구함
            ans = N_list[i]

    print(f'#{k} {ans}')