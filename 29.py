import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

n = int(input())
A = list(map(int, input().split()))
q = int(input())
B = list(map(int, input().split()))

def bisearch(x):        # x의 인덱스 반환
    s, e = 0, n-1
    while s<=e:
        mid = (s+e)//2
        if A[mid] == x: return mid
        elif A[mid] < x: s = mid+1
        else: e = mid - 1
    return -1

for x in B:
    print(bisearch(x), end=' ')

# def lowerbound(x):        # x보다 크거나 같은 가장 작은 값 반환, 없으면 -1
#     s, e = 0, n-1
#     while s<=e:
#         mid = (s+e)//2
#         if A[mid] >= x: e = mid - 1
#         else: s = mid + 1
#     return A[s] if s<n else -1
#
# print()
# for x in B:
#     print(lowerbound(x), end=' ')