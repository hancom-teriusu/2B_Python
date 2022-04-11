import sys
from collections import deque
sys.stdin = open('input.txt')
input = sys.stdin.readline

dq = deque()

def insertF(pos, value):
    if pos==1:
        dq.append(value)        # O(1)
    else:
        dq.appendleft(value)    # O(1)

def eraseF(pos, value):
    cnt = 0
    if pos==0:
        i = 0
        while i < len(dq):
            if dq[i]>=value:
                del dq[i]           # O(N)
                cnt+=1
                if cnt>=3: break
            else:
                i+=1

    else:
        i = len(dq) - 1
        while i>=0 and cnt<3:
            if dq[i]>=value:
                del dq[i]           # O(N)
                cnt+=1
            i-=1

def sortF(value):
    global dq
    #dq = deque(sorted(dq, key=abs))
    dq = deque(sorted(dq, key=lambda x : [abs(x-value), x]))

def printF(pos):
    if pos==0:
        print(*dq)
    else:
        print(*reversed(dq))

q = int(input())
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0]==1: insertF(cmd[1], cmd[2])
    elif cmd[0]==2: eraseF(cmd[1], cmd[2])
    elif cmd[0]==3: sortF(cmd[1])
    else: printF(cmd[1])