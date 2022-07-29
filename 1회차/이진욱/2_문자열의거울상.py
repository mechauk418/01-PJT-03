import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())

for k in range(1,T+1):

    S = input()

    S_grab = S[::-1] # 문자열을 역순으로 뒤집음.
    ans = '' # 정답을 초기화

    for i in S_grab:
        if i == 'b':
            ans += 'd' # b가 나오면 정답에 d를 더해줌
        elif i == 'd':
            ans += 'b' # d가 나오면 정답에 b를 더해줌
        elif i == 'p':
            ans += 'q' # p가 나오면 정답에 q를 더해줌
        else:
            ans += 'p' # q가 나오면 정답에 p를 더해줌

    print(f'#{k} {ans}')
