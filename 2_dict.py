import sys
from heapq import nlargest

sys.stdin=open('input.txt')
#input=sys.stdin.readline
#input() => sys.stdin.readline()


#D = dict()
D = {}

# range(3) : 0, 1, 2
# range(1,3) : 1, 2
# range(3, 10, 2) : 3, 5, 7, 9

for _ in range(int(input())):
    cmd = input().split()
    data = list(map(int, cmd[1:]))
    if cmd[0] == 'register':
        D[data[0]] = data[1:]   # key=data[0] , value=data[1:] , [salary, C, J, P]

    elif cmd[0] == 'cancel':
        if data[0] in D:
            del D[data[0]]

    elif cmd[0] == 'update':
        pid, flag, X = data
        if pid in D:
            D[pid][flag+1] = X


    elif cmd[0] == 'hire_min':
        # 1.salary 작은순, 2.pid 작은순
        # 1.value[0]    , 2.key
        pid = min(D.items(), key=lambda item : [item[1][0], item[0]])[0]
        print(pid)
        del D[pid]

    else:
        ## O(n * 3)
        # for _ in range(3):
        #     pid = max(D.items(), key=lambda item : [sum(item[1][1:]), item[0]])[0]
        #     print(pid, end=' ')
        #     del D[pid]
        # print()

        ## O(n + 3 log n)
        best = nlargest(3, D.items(), key=lambda item : [sum(item[1][1:]), item[0]])
        for pid, _ in best:
            print(pid, end= ' ')
            del D[pid]
        print()

# li = [12,-23,-124,23]
# print(min(li, key=abs))
#
# d = {1:123, 2:1, 3:4}
# print(d.items())
# print(d.keys())
# print(d.values())
