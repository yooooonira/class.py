import sys
input=sys.stdin.readline
num=int(input().strip())

dp = [0] * (num+1)
# 최소 연산 횟수를 저장하는 리스트
# dp[1]은 1의 최소 연산 횟수 ... 

for i in range(2, num+1):
    # dp[1]은 연산횟수가 1번이니까 2부터
    dp[i] = dp[i-1] + 1  
    # -1값을 기본값으로 두기
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
        
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)

print(dp[num])
