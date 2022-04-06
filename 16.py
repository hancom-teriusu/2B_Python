import sys
import time
from heapq import heappop, heappush

sys.stdin = open('input.txt')
input = sys.stdin.readline

maxpq, minpq, abspq = [], [], []

start = time.process_time()

for _ in range(int(input())):
    x = int(input())
    if x==0:
        if minpq: print(-heappop(maxpq), heappop(minpq), heappop(abspq)[1])
        else: print(-1)
    else:
        heappush(minpq, x)
        heappush(maxpq, -x)
        heappush(abspq, (abs(x), x))

# for x in range(10000000):
#     if x%5==0: x = 0
#     if x==0:
#         if minpq:
#             heappop(maxpq) #, heappop(minpq), heappop(abspq)
#     else:
#         #heappush(minpq, x)
#         #heappush(maxpq, (-x,-x))
#         heappush(abspq, [abs(x), x])


print('time: ', time.process_time() - start)