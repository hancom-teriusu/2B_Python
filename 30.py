import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n, m = map(int, input().split())
A = list(map(int, input().split()))

def check(limit):
    groupCnt = 1
    groupSum = 0
    for x in A:
        groupSum += x
        if groupSum > limit:
            groupCnt += 1
            groupSum = x
        if groupCnt > m: return 0
    return 1

s, e = max(A), sum(A)
while s <= e:
    mid = (s+e)//2
    if check(mid): e = mid - 1
    else: s = mid + 1

print(s)