import sys
#sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = [0] * n         # [0:n]

def isBad(len):
    for i in range(1, len//2 + 1):
        if A[len-i:len] == A[len-i*2:len-i]:
            return 1
    return 0

def recur(x):
    if x>=n:
        print(*A, sep='')
        return 1

    for i in range(1,4):
        A[x] = i
        if isBad(x+1): continue
        success = recur(x+1)
        if success: return 1

    return 0

recur(0)