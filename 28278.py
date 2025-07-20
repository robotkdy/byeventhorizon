import sys
input = sys.stdin.readline

n = int(input())

d = []
st = []

for a in range(n):
    l= list(map(int,input().split()))
    if l[0] == 1:
        st.append(l[1])
    elif l[0] == 2:
        if len(st) != 0:
            print(st.pop())
        else:
            print(-1)
    elif l[0] == 3:
        print(len(st))
    elif l[0] == 4:
        if len(st) == 0:
            print(1)
        else:
            print(0)
    elif l[0] == 5:
        if len(st) != 0:
            print(st[-1])
        else:
            print(-1)
