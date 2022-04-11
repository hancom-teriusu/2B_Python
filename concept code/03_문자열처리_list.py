import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

li = []
# str, < : 사전순으로 빠르면 작다
for _ in range(int(input())):
    cmd, val = input().split()
    if cmd=='1':
        li.append(val.lower())
    elif cmd=='2':
        if val=='0': li.sort()  # < , 사전순 빠른 순
        elif val=='1': li.sort(reverse=1)
        else: li.sort(key=lambda x: [len(x), x])
        print(*li[:3])
    else:
        li[0] += val.lower()
        li[0] = li[0][:15]
        print(li[0])