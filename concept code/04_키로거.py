import sys

sys.stdin = open('input.txt')
input = sys.stdin.readline

# left group : 뒤쪽 원소 삽입/삭제      list
# right group : 앞쪽 원소 삽입/삭제     deque/list(역)

L, R = [], []

for _ in range(int(input())):
    log = input().strip()
    L.clear()
    R.clear()

    for x in log:
        if x=='<':
            if L: R.append(L.pop())
        elif x == '>':
            if R: L.append(R.pop())
        elif x == '-':
            if L: L.pop()
        else:
            L.append(x)
    print(''.join(L + R[::-1]))


# str type : immutable
#
# s = 'abc'
# s += 'def'
# s => 'abcdef' , 새롭게 문자열 생성