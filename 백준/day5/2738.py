import sys

n,m=map(int,sys.stdin.readline().split())

matrixA=[]
for i in range(n):
    matrixA.append(list(map(int,sys.stdin.readline().split())))

matrixB=[]
for i in range(n):
    matrixB.append(list(map(int,sys.stdin.readline().split())))

result=[]
for i in range(n):
    middle=[]
    for j in range(m):
        middle.append(matrixA[i][j]+matrixB[i][j])
    result.append(middle)

for i in result:
    print(*i)
