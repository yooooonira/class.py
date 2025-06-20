import sys

N,K=map(int, sys.stdin.readline().split())

coins=[]
cnt=0

for _ in range(N):
    coin=int(sys.stdin.readline().strip())
    coins.append(coin)

coins.sort(reverse=True)

for coin in coins:
    if K>=coin:
        cnt+=K//coin
        K %=coin


print(cnt)
