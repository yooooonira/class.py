def solution(a, b, n):
    cnt=0
    while n>=a:
        exchange = n//a
        n -= (exchange)*a
        n += (exchange)*b
        cnt += exchange *b 
    return cnt
