import sys
from collections import defaultdict
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline

htab = defaultdict(int)
maxpq, minpq = [], []

for _ in range(int(input())):
    cmd, X, cnt = map(int, input().split())
    if cmd==1:
        htab[X]+=cnt
        heappush(minpq, X)
        heappush(maxpq, -X)

        print(htab[X])

    elif cmd==2:
        htab[X]-=cnt
        if htab[X]<=0:
            del htab[X]
            print(0)
        else:
            print(htab[X])

    else:
        worthSum = 0
        pq = maxpq if X else minpq     # reference copy
        while pq and cnt:
            worth = abs(pq[0])
            if worth not in htab:
                heappop(pq)
                continue

            sellCnt = min(cnt, htab[worth])
            cnt -= sellCnt
            htab[worth] -= sellCnt

            if htab[worth]==0:
                del htab[worth]
                heappop(pq)

            worthSum += worth * sellCnt

        print(worthSum)


