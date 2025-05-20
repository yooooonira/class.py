from sys import stdin

n=int(stdin.readline())
a=list(map(int, stdin.readline().split()))
v=int(stdin.readline())

cnt=0
for i in a:
    if i == v:
        cnt+=1
print(cnt)
