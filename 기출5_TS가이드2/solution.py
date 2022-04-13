# nlargest

from heapq import nlargest, nsmallest
from typing import List

userXY = []
class Cafe:
    def __init__(self, dist):
        self.myOrder = 0
        self.totOrder = 0
        self.dist = dist
global buddy, user
n = 0

def init(N: int, px: List[int], py: List[int]) -> None:
    global n, buddy, user
    n = N
    buddy = [[] for _ in range(n)]  # buddy[uid] = [uid2, uid3, .., ]
    user = [{} for _ in range(n)]   # user[uid] = { cid: Cafe() , .., }
    userXY.clear()
    for x, y in zip(px, py):
        userXY.append((x,y))

def addCafe(cid: int, x: int, y: int) -> None:
    for i in range(n):
        user[i][cid]=Cafe(abs(x-userXY[i][0])+abs(y-userXY[i][1]))

def eraseCafe(cid: int) -> None:
    for i in range(n):
        del user[i][cid]

def order(uid: int, cid: int) -> None:
    user[uid][cid].myOrder += 1
    user[uid][cid].totOrder += 1
    for x in buddy[uid]:
        user[x][cid].totOrder += 1

def beBuddy(tid: int, uid: int) -> None:
    buddy[uid].append(tid)
    buddy[tid].append(uid)
    for cid in user[uid].keys():
        user[uid][cid].totOrder += user[tid][cid].myOrder
        user[tid][cid].totOrder += user[uid][cid].myOrder

def recommend(uid: int) -> int:
    #1
    return nlargest(10,user[uid].keys(),key=lambda x: (user[uid][x].totOrder, -user[uid][x].dist, -x))[9]

    #2
    # 1) 주문 많은순   2) 거리 짧은순   3) cid 작은순
    #    a=0 ~ 3000     b=0 ~ 4,000,000   c=0 ~ 999,999
    #   ____ _______ ______
    #   (3000-a)*10^13 + b*10^6 + c
    li = [(3000 - y.totOrder) * int(1e+13) + y.dist * int(1e+6) + x for x, y in user[uid].items()]
    return nsmallest(10, li)[9] % 1000000

