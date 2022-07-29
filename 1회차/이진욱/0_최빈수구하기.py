import sys, collections

sys.stdin = open("_최빈수구하기.txt")

T = int(input())

for i in range(T):
    N = int(input())
    N_list = list(map(int,input().split()))

    dict1 = collections.Counter(N_list) 

    dic_value = [k for k,v in dict1.items() if max(dict1.values()) == v]

    ans = max(dic_value)

    print( f'#{i+1} {ans}' )




