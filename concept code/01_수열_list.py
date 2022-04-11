import sys
sys.stdin = open('input.txt')

li = []
li2 = list()

def insertF(pos, value):
    global li
    if pos==1:
        li.append(value)        # O(1)
        #li+=[value]
    else:
        li.insert(0, value)     # O(N)

def eraseF(pos, value):
    global li
    cnt = 0
    if pos==0:
        i = 0
        while i < len(li):
            if li[i]>=value:
                del li[i]           # O(N)
                cnt+=1
                if cnt>=3: break
            else:
                i+=1

    else:
        i = len(li) - 1
        while i>=0 and cnt<3:
            if li[i]>=value:
                del li[i]           # O(N)
                cnt+=1
            i-=1

def comp(x):
    return abs(x)

def sortF(value):
    li.sort()           # default : '<'         O(N log N)
    li.sort(reverse=1)
    #li.sort(key=comp)
    li.sort(key=lambda x : [abs(value-x), x])

def printF(pos):
    if pos == 0:
        #for x in li: print(x, end=' ')
        #print()
        print(*li)
    else:
        print(*li[::-1])

q = int(input())
for _ in range(q):
    cmd = list(map(int, input().split()))
    if cmd[0]==1: insertF(cmd[1], cmd[2])
    elif cmd[0]==2: eraseF(cmd[1], cmd[2])
    elif cmd[0]==3: sortF(cmd[1])
    else: printF(cmd[1])