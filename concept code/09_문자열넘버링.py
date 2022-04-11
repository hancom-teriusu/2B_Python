import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

D = {}
idcnt = 0

for _ in range(int(input())):
    name, score = input().split()
    name = name.lower()
    score = int(score)

    if name not in D:
        idcnt+=1
        D[name] = [idcnt, score]
    else:
        D[name][1] = max(D[name][1], score)

    print(D[name][0], D[name][1])