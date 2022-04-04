import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M, Q = map(int,input().split())
memo = [deque() for _ in range(N)]
cur, cnt = 0, 0

for c in input().strip():
    memo[cnt // M].append(c)
    cnt+=1

for _ in range(Q):
    cmd = input().split()
    if cmd[0]=='insert':
        x, y = cur // M, cur % M
        memo[x].insert(y, cmd[1])
        while len(memo[x]) > M:
            memo[x+1].appendleft(memo[x].pop())
            x+=1
        cur+=1
        cnt+=1

    elif cmd[0]=='erase':
         if cur==0: continue
         cur-=1
         cnt-=1
         x, y = cur // M, cur % M
         del memo[x][y]
         while memo[x+1]:
             memo[x].append(memo[x+1].popleft())
             x+=1

    else:
        x, y = map(int, cmd[1:])
        cur = min(cnt, x * M + y)
        print('*' if cur==cnt else memo[x][y])