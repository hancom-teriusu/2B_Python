import sys
from collections import defaultdict

sys.stdin = open('input.txt')
input = sys.stdin.readline

prefix = set()
wordCnt = defaultdict(int)

for _ in range(int(input())):
    word = input().strip()
    s = ""
    ret = ""
    for c in word:
        s+=c
        if s not in prefix:
            if ret=="": ret = s
            prefix.add(s)
    wordCnt[word]+=1

    # if ret=="":
    #     if wordCnt[word]>1: print(word, wordCnt[word], sep='')
    #     else: print(word)
    # else:
    #     print(ret)

    if ret=='':
        ret = word
        if wordCnt[word]>1: ret+=str(wordCnt[word])
    print(ret)
