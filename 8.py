import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

D = {} # dict
S = set()

for _ in range(int(input())):
    string = input().strip()
    if string in S:
        S.remove(string)
    else:
        S.add(string)

print(len(S))
