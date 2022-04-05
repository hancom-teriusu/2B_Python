import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K, string = int(input()), input().strip()
D = defaultdict(int)
key = [0] * 4  # [a, c, g, t]
idx = {'A':0, 'C':1, 'G':2, 'T':3}

for i in range(len(string)):
    key[idx[string[i]]]+=1
    if i>=K: key[idx[string[i-K]]]-=1
    D[tuple(key)]+=1

print(max(D.values()))