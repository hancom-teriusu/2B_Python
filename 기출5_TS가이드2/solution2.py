# heapq , key=tuple

from heapq import heappush, heappop
from typing import List

class Cafe:
    def __init__(self, dist):
        self.myOrder = 0
        self.totOrder = 0
        self.dist = dist

def init(N: int, px: List[int], py: List[int]) -> None:
    global n, buddy, user, pq, userXY
    n = N
    buddy = [[] for _ in range(n)]
    pq = [[] for _ in range(n)]
    user = [{} for _ in range(n)]
    userXY = list(zip(px, py))

def push(uid, cid):
    heappush(pq[uid], (-user[uid][cid].totOrder, user[uid][cid].dist, cid))

def addCafe(cid: int, x: int, y: int) -> None:
    for i in range(n):
        user[i][cid]=Cafe(abs(x-userXY[i][0])+abs(y-userXY[i][1]))
        push(i, cid)

def eraseCafe(cid: int) -> None:
    for i in range(n):
        del user[i][cid]

def order(uid: int, cid: int) -> None:
    user[uid][cid].myOrder += 1
    user[uid][cid].totOrder += 1
    push(uid, cid)
    for x in buddy[uid]:
        user[x][cid].totOrder += 1
        push(x,cid)

def beBuddy(tid: int, uid: int) -> None:
    buddy[uid].append(tid)
    buddy[tid].append(uid)
    for cid in user[uid].keys():
        if user[tid][cid].myOrder:
            user[uid][cid].totOrder += user[tid][cid].myOrder
            push(uid,cid)
        if user[uid][cid].myOrder:
            user[tid][cid].totOrder += user[uid][cid].myOrder
            push(tid,cid)

def recommend(uid: int) -> int:
    best = []
    while len(best) < 10:
        cnt, dist, cid = heappop(pq[uid])
        if cid not in user[uid] or abs(cnt) != user[uid][cid].totOrder: continue
        # 중복처리는 안함 : {uid, cid} cnt가 동일한데 push되는 경우는 없음
        best.append((cnt,dist,cid))
    for data in best: heappush(pq[uid], data)
    return best[9][2]
