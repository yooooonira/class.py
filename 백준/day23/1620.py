import sys
N,M=map(int, sys.stdin.readline().split())

#시간초과가 뜨니 리스트를 쓰지 말자
strdata={}
intdata={}
for i in range(1,N+1):
    name=sys.stdin.readline().strip()
    strdata[str(i)]=name
    intdata[name]=i

for _ in range(M):
    command=sys.stdin.readline().strip()
    if command.isdigit(): 
        print(strdata[command])
    else: 
        print(intdata[command])
