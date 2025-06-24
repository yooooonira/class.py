import sys
input=sys.stdin.readline
T=int(input().strip())
memo={}
def fibonacci(n):
    if n in memo:
        return memo[n]

    if n==0:
        memo[n]=(1,0)
    elif n==1:
        memo[n]=(0,1)
    else:
        cntZ1, cntO1=fibonacci(n-1)
        cntZ2, cntO2=fibonacci(n-2)
        memo[n]=(cntZ1+cntZ2, cntO1+cntO2)
    return  memo[n]

cntZ,cntO=0,0
for _ in range(T):
    num=int(input().strip())
    (cntZ,cntO)=fibonacci(num)
    print(f"{cntZ} {cntO}")
