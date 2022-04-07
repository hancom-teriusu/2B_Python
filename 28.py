import sys
from collections import deque

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, K = map(int, input().split())
code = [''] + [ input().strip() for _ in range(n) ]
adj = [[] for _ in range(n+1)]
visited = [0] * (n+1)
prev = [0] * (n+1)

for i in range(1, n+1):     # 그래프 구성
    for j in range(1, i):
        diff = 0
        for k in range(K):
            diff += code[i][k] != code[j][k]
        if diff==1:
            adj[i].append(j)
            adj[j].append(i)

def printPath(x):
    path = []
    while x:
        path.append(x)
        x = prev[x]
    print(*path[::-1])

def printRecur(x):
    if x==0: return
    printRecur(prev[x])
    print(x, end=' ')

def bfs(s, e):
    q = deque([s])
    visited[s] = 1

    while q:
        x = q.popleft()
        for y in adj[x]:
            if visited[y]: continue
            q.append(y)
            visited[y] = 1
            prev[y] = x
            if y==e:
                printPath(y)
                #printRecur(y)
                return
    print(-1)

bfs(*map(int, input().split()))