import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

w, h = map(int,input().split())
A = [ input().strip() for _ in range(h) ]
visited = [[0]*w for _ in range(h)]
dx, dy = [-1,0,1,0], [0,1,0,-1]
#dxy = [(-1,0), (0,1), (1,0), (0,-1)]

def dfs(x,y):
    if x<0 or x>=h or y<0 or y>=w: return 0
    if visited[x][y]: return 0
    if A[x][y]=='.': return 0

    cnt = 1
    visited[x][y] = 1

    for i in range(4):
        cnt += dfs(x+dx[i], y+dy[i])

    return cnt


ret = 0
for i in range(h):
    for j in range(w):
        ret = max(ret, dfs(i,j))

print(ret)