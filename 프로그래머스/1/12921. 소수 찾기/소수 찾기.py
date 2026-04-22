def solution(n):
    cnt=0
    for i in  range(2,n+1):
        # for j in  range(2,i):
        for j in range(2, int(i**0.5) + 1):
            if i%j==0:
                break
        else:  # for-else (break 안 걸렸을 때만 실행)
            cnt += 1
    return cnt