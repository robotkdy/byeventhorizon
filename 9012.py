import sys
input = sys.stdin.readline

n = int(input())

def solve():
    s = input().rstrip()
    st = []
    for c in s:
        if c == "(":
            st.append(c)
        else:
            if len(st)==0:
                return False
            else:
                st.pop()
    if len(st)==0:
        return True
    else:
        return False

for _ in range(n):
    if solve():
        print("YES")
    else:
        print("NO")