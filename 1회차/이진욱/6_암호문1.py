import sys

sys.stdin = open("_암호문1.txt")


for k in range(1,11):

    N_len = int(input()) # 암호문의 길이

    S_list = list(map(str,input().split())) # 원본 암호문

 
    N_com = int(input()) # 명렁어의 갯수

    S_com = list(map(str,input().split())) # 명령어를 공백 단위로 리스트에 넣음

    for i in range(len(S_com)): # 명령어 리스트를 순회한다.
        if S_com[i] == 'I': # I를 만나면 아래와 같은 코드를 실행
            for j in range(int(S_com[i+2])): # S_com[i+2] = y. 원본 암호문에 y개를 넣기위해 y번 반복한다.
                S_list.insert(int(S_com[i+1])+j,S_com[i+3+j]) # x위치에 s의 코드를 넣어줌.

    print(f'#{k} {" ".join(S_list[0:10])}')