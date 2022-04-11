import sys
from heapq import heappush, heappop

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
mid = int(input())
print(mid)

left = []   # maxpq
right = []  # minpq
for i in range(n//2):
    for x in map(int,input().split()):
        heappush(left, -x) if x < mid else heappush(right, x)

    if len(left) < len(right):
        heappush(left, -mid)
        mid = heappop(right)
    elif len(left) > len(right):
        heappush(right, mid)
        mid = -heappop(left)

    print(mid)