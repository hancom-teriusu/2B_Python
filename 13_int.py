import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

K, string = int(input()), input().strip()
D = defaultdict(int)
key = 0
base = {'A':1001**3, 'C':1001**2, 'G':1001, 'T':1}

for i in range(len(string)):
    key += base[string[i]]
    if i>=K: key -= base[string[i-K]]
    D[key]+=1

print(max(D.values()))