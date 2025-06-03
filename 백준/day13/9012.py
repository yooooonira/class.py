import sys

def check(prnth):
    stack = []
    for ch in prnth:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if not stack:
                return "NO"
            stack.pop()
    return "YES" if not stack else "NO"

n = int(sys.stdin.readline())
for i in range(n):
    prnth = sys.stdin.readline().strip()
    print(check(prnth))
