import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

parent = [0] + [-1] * 10000
child = [set() for _ in range(10001)]

def isParent(x, y):             # y의 조상노드에 x가 있는지 판별
    while 1:
        if y == x: return 1
        if y == 0: return 0
        y = parent[y]

def getA(x):                    # x와 root노드와의 거리
    cnt = 0
    while x:
        cnt += 1
        x = parent[x]
    return cnt

def getB(x):                    # x와 가장 먼 자손노드와의 거리
    ret = 0
    for y in child[x]:
        ret = max(ret, getB(y) + 1)
    return ret

def getC(x):                    # x를 포함한 모든 자손(자식)노드 개수
    cnt = 1
    for y in child[x]:
        cnt += getC(y)
    return cnt

for _ in range(int(input())):
    cmd = input().split()
    if cmd[0]=='add':
        x, y = map(int, cmd[1:])
        parent[x] = y
        child[y].add(x)
    elif cmd[0]=='remove':
        x = int(cmd[1])
        if x==0 or parent[x] == -1: continue
        child[parent[x]] |= child[x]
        child[parent[x]].remove(x)
        for cid in child[x]: parent[cid] = parent[x]
        parent[x] = -1
    elif cmd[0]=='move':
        x, y = map(int,cmd[1:])
        if parent[x]==-1 or parent[y]==-1 or x==y: continue
        if isParent(x, y): continue

        child[parent[x]].remove(x)
        #child[parent[x]] -= {x}

        parent[x] = y
        child[y].add(x)
    else:
        x = int(cmd[1])
        print(getA(x), getB(x))
        print(getC(x))
