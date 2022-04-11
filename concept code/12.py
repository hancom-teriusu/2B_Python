import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n,q = map(int,input().split())
D = {}
cnt = [0] * 4

for i in range(q):
    pid = i % 4
    #key = tuple(map(int,input().split()))
    x, y = map(int, input().split())
    key = x * n + y
    if key in D:
        pid2 = D[key]
        if pid==pid2:
            del D[key]
            cnt[pid]-=1
        elif cnt[pid] < cnt[pid2]:
            D[key] = pid
            cnt[pid]+=1
            cnt[pid2]-=1
    else:
        D[key] = pid
        cnt[pid]+=1

for x in cnt: print(x)