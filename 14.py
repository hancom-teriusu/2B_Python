import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = [input().strip() for _ in range(n)]

################# hash table 등록 ######################
htab = [[] for _ in range(2**16)]
def gethash(arr, x, y):
    hash = 0
    for i in range(4):
        for j in range(4):
            hash = hash * 2 + int(arr[x+i][y+j]=='+')
    return hash

for i in range(n-3):
    for j in range(n-3):
        htab[gethash(A,i,j)].append((i,j))
#######################################################

def check(x,y):
    if x+m > n or y+m > n: return 0
    for i in range(m):
        if A[x+i][y:y+m] != B[i]: return 0
    return 1

for _ in range(int(input())):
    m = int(input())
    B = [input().strip() for _ in range(m)]

    ######### hash table 검색
    hash = gethash(B, 0, 0)
    cnt = 0
    for x,y in htab[hash]:
        if check(x,y): cnt+=1
    print(cnt)