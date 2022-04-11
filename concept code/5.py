import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

N = int(input())

#dice[주사위 번호 0 ~ N-1][주사위 값 1 ~ 6] = 반대 값
#dice = [[0] * 7] * N   # list: mutable , reference copy X

#dice = [[x for x in range(7)] for _ in range(N)]
dice = [[0] * 7 for _ in range(N)]

for i in range(N):
    a,b,c,d,e,f = map(int, input().split())
    for x,y in [[a,f],[b,d],[c,e]]:
        #dice[i][x] = y
        #dice[i][y] = x
        dice[i][x], dice[i][y] = y, x

ret = 0
for bottom in range(1,7):
    sum = 0
    for i in range(N):
        top = dice[i][bottom]
        # for j in range(6,0,-1):
        #    if top != j and bottom != j:
        #        sum+=j
        #

        sum += max(range(1,7), key=lambda x: 0 if x in [top, bottom] else x)

        bottom = top
    ret = max(ret, sum)
print(ret)