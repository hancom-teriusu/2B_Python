import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline

S = [0] * 100003    # S[id] = score
minpq, maxpq = [], []

def getMin():
    valid = []  # (score, id)
    while minpq and len(valid) < 3:
        score, id = heappop(minpq)
        if score != S[id]: continue
        if valid and valid[-1][1] == id: continue
        valid.append((score,id))

    if len(valid)==3: print(valid[2][1])
    else: print(-1)

    for t in valid: heappush(minpq, t)

def getMax():
    valid = []  # (score, id)
    while maxpq and len(valid) < 3:
        score, id = map(abs,heappop(maxpq))
        if score != S[id]: continue
        if valid and valid[-1][1] == id: continue
        valid.append((score,id))

    if len(valid)==3: print(valid[2][1])
    else: print(-1)

    for t in valid: heappush(maxpq, (-t[0], -t[1]))

def get(pq):
    valid = []  # (score, id)
    while pq and len(valid) < 3:
        score, id = heappop(pq)
        if abs(score) != S[abs(id)]: continue
        if valid and valid[-1][1] == id: continue
        valid.append((score,id))

    if len(valid)==3: print(abs(valid[2][1]))
    else: print(-1)

    for t in valid: heappush(pq, t)


for _ in range(int(input())):
    cmd = list(map(int, input().split()))
    if cmd[0]==1:
        id, score = cmd[1:]
        heappush(minpq, (score, id))
        heappush(maxpq, (-score, -id))
        S[id] = score

    elif cmd[0]==2:
        S[cmd[1]] = 0

    elif cmd[0]==3: get(minpq)  #getMin()
    else: get(maxpq)            #getMax()
