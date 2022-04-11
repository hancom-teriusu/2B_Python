import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

w, h = map(int,input().split())
A = [ input().strip() for _ in range(h) ]
visited = [[0]*w for _ in range(h)]
dx, dy = [-1,0,1,0], [0,1,0,-1]

def bfs(x,y):
    que = deque([(x,y)])
    visited[x][y] = 1
    cnt = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]
            if nx<0 or nx>=h or ny<0 or ny>=w: continue
            if A[nx][ny]=='.' or visited[nx][ny]: continue

            visited[nx][ny] = 1
            cnt+=1
            que.append((nx,ny))

    return cnt

ret = 0
for i in range(h):
    for j in range(w):
        if A[i][j]=='*' and visited[i][j]==0:
            ret = max(ret, bfs(i,j))


print(ret)