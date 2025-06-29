import sys
input=sys.stdin.readline
num=int(input().strip()) #1~num
cn_num=int(input().strip())

cn=[ [] for _ in range(num+1)]

for _ in range(cn_num):
    a,b=map(int,input().split())
    cn[a].append(b)
    cn[b].append(a)

visited = [False] * (num + 1) #미방문으로 초기화 

def dfs(x): #Breadth-First Search
    visited[x] = True
    for i in cn[x]: #ex) [2, 5]
        if not visited[i]:
            dfs(i)

dfs(1) 
print(visited.count(True) - 1)
