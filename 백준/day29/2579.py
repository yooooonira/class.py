# DP
import sys
input=sys.stdin.readline
num=int(input().strip())
scores = [0] + [int(input()) for _ in range(num)]

dp=[0]*(num+1)   #dp -> 계단 당 최대 누적
if num>=1:
    dp[1]=scores[1]
if num>=2:
    dp[2] = scores[2] + scores[1]
if num>=3:
    for i in range(3,num+1): 
        dp[i] = max(dp[i-2] + scores[i], dp[i-3] + scores[i-1] + scores[i])
print(dp[num])
