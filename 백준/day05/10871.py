from sys import stdin

n,x=map(int,stdin.readline().split())
a=list(map(int, stdin.readline().split()))

for i in a:
    if i <x:
        print(i,end=" ")
