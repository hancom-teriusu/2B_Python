import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

m, n = map(int, input().split())
A = [ list(input().strip()) for _ in range(n)]
sy, sx = map(int, input().split())
dx, dy = [-1,0,1,0], [0,1,0,-1]

def bfs(sx, sy):
    q = deque([(sx, sy, 3)])
    A[sx][sy] = '0'
    while q:
        x, y, tick = q.popleft()
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=n or ny<0 or ny>=m: continue
            if A[nx][ny]=='0': continue
            q.append((nx, ny, tick+1))
            A[nx][ny] = '0'
    return tick

print(bfs(sx-1, sy-1))

ret = 0
for i in range(n):
    ret += sum(map(int, A[i]))
print(ret)

# print(sum([sum(map(int, A[i])) for i in range(n)]))