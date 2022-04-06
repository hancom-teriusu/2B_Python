import sys
from collections import defaultdict
from heapq import heappush, heappop
sys.stdin = open('input.txt')
input = sys.stdin.readline

maxsum, minsum, maxavg, minavg = [], [], [], []

n, m = map(int, input().split())
S = defaultdict(dict)   # S[sid] = dict{key:pid, value:score}
nameDict = {}
class Player:
    sum, avg, cnt = 0,0,0
    def update(self, dsum, dcnt):
        self.sum += dsum
        self.cnt += dcnt
        self.avg = round(self.sum / self.cnt, 1) if self.cnt else 0

    def __repr__(self):        return '('+str(self.sum)+ ',' + str(self.avg)+','+str(self.cnt)+')'
P = {}  # P[name] = Player()

class MaxData:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, rhs):  # <
        if self.priority != rhs.priority:
            return self.priority > rhs.priority
        return self.name > rhs.name

class MinData:
    def __init__(self, priority, name):
        self.priority = priority
        self.name = name
    def __lt__(self, rhs):  # <
        if self.priority != rhs.priority:
            return self.priority < rhs.priority
        return self.name < rhs.name

def push(pname):
    heappush(maxsum, MaxData(P[pname].sum, pname))
    heappush(minsum, MinData(P[pname].sum, pname))
    heappush(maxavg, MaxData(P[pname].avg, pname))
    heappush(minavg, MinData(P[pname].avg, pname))

for pname in input().split():
    P[pname] = Player()
    push(pname)

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        if pname in S[sid]: P[pname].update(score-S[sid][pname], 0)
        else: P[pname].update(score, 1)
        S[sid][pname] = score
        push(pname)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pname, score in S[sid].items():
            P[pname].update(-score, -1)
            push(pname)
        S[sid].clear()

    elif cmd[0]=='SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while pq[0].priority != P[pq[0].name].sum: heappop(pq)
        print(pq[0].name)

    else:
        pq = maxavg if cmd[1] == '1' else minavg
        while pq[0].priority != P[pq[0].name].avg: heappop(pq)
        print(pq[0].name)
