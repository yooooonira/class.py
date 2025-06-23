import sys
input=sys.stdin.readline
time=0
n=int(input().strip())
sequence=list(map(int,input().split()))
sequence.sort()

result=[]
for i in sequence:
    time=time+i
    result.append(time)
print(sum(result))
