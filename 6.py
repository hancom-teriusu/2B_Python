import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

li = []
for _ in range(int(input())):
    li.append(list(map(int,input().split())))
li.sort(key=lambda data : data[2])

ret = []
end = 0
for id, s, e in li:
    if end <= s:
        ret.append(id)
        end = e
print(len(ret))
print(*ret)