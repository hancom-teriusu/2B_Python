import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int,input().split())

# for i in range(1,7):
#     for j in range(i if m==2 else 1, 7):
#         if m==3 and i==j: continue
#         for k in range(j if m==2 else 1, 7):
#             if m==3 and (i==k or j==k): continue
#             print(i, j, k)

dice = [1] * (n+1)
used = [0] * 7      # used[x] = 1 : x 숫자 사용
def recur(x):   # x번째 주사위 결정

    ''' base condition '''
    if x>n:
        print(*dice[1:])
        return

    ''' normal condition '''
    for i in range(1 if m!=2 else dice[x-1], 7):
        #if i in dice[1:x]: continue     # O(n)
        if m==3 and used[i]: continue    # O(1)

        dice[x] = i
        used[i] = 1
        recur(x+1)
        used[i] = 0

recur(1)