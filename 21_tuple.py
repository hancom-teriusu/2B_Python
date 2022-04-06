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
    name = ""
    def update(self, dsum, dcnt):
        self.sum += dsum
        self.cnt += dcnt
        self.avg = round(self.sum / self.cnt, 1) if self.cnt else 0

    def __repr__(self):        return '('+str(self.sum)+ ',' + str(self.avg)+','+str(self.cnt)+')'
P = [Player() for _ in range(m+1)]

def push(pid):
    heappush(maxsum, (-P[pid].sum, -pid))
    heappush(minsum, (P[pid].sum, pid))
    heappush(maxavg, (-P[pid].avg, -pid))
    heappush(minavg, (P[pid].avg, pid))

name = input().split()
name.sort()
for i in range(1, m+1):
    nameDict[name[i-1]] = i   # 1부터 id부여
    P[i].name=name[i-1]
    push(i)

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='EVAL':
        sid, pname, score = int(cmd[1]), cmd[2], int(cmd[3])
        pid = nameDict[pname]
        if pid in S[sid]: P[pid].update(score-S[sid][pid], 0)
        else: P[pid].update(score, 1)
        S[sid][pid] = score
        push(pid)

    elif cmd[0]=='CLEAR':
        sid = int(cmd[1])
        for pid, score in S[sid].items():
            P[pid].update(-score, -1)
            push(pid)
        S[sid].clear()

    elif cmd[0]=='SUM':
        pq = maxsum if cmd[1]=='1' else minsum
        while abs(pq[0][0]) != P[abs(pq[0][1])].sum: heappop(pq)
        print(P[abs(pq[0][1])].name)

    else:
        pq = maxavg if cmd[1] == '1' else minavg
        while abs(pq[0][0]) != P[abs(pq[0][1])].avg: heappop(pq)
        print(P[abs(pq[0][1])].name)