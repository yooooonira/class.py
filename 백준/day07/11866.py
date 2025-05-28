import sys

n,k = map(int,sys.stdin.readline().split())

setting= [i for i in range(1,n+1)]
result=[]

idx = 0  
for i in range(n):
    idx = (idx + k - 1) % len(setting)  
    result.append(setting[idx])
    del setting[idx]


print(f"<{', '.join(map(str, result))}>")

#print(f"<{*result}>")  --> f포맷출력문에서 *list 같은 전개 연산자 불가, print문에서는 가능 
