import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

w, h = map(int,input().split())
A = [ input().strip() for _ in range(h) ]
visited = [[0]*w for _ in range(h)]
dx, dy = [-1,0,1,0], [0,1,0,-1]
#dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(x,y):
    cnt = 1
    visited[x][y] = 1

    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx < 0 or nx >= h or ny < 0 or ny >= w: continue
        if visited[nx][ny]: continue
        if A[nx][ny] == '.': continue

        cnt += dfs(nx, ny)

    return cnt


ret = 0
for i in range(h):
    for j in range(w):
        if A[i][j]=='*' and visited[i][j]==0:
            ret = max(ret, dfs(i,j))

print(ret)