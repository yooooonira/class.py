from math import gcd
# 최대공약수(Greatest Common Divisor)

def lcm(a, b): # Least Common Multiple
    return a * b // gcd(a, b)

def solution(signals):
    # t = 1
    # while True:
    #     if all((g < (t) % (g+y+r) <= g+y)for g, y, r in signals):
    #         return t
    #     t += 1
    
    # 전체 주기
    limit = 1
    for g, y, r in signals:
        limit = lcm(limit, g + y + r)

    # 기준 신호등
    g0, y0, r0 = signals[0]
    cycle0 = g0 + y0 + r0

    # 후보 t 생성
    k = 0
    while True:
        base = k * cycle0

        for offset in range(g0, g0 + y0):  # 노란 구간
            t = base + offset + 1  # (t-1 기준이라 +1)

            if t > limit:
                return -1

            # 모든 신호등 검사
            if all(
                g <= (t-1) % (g+y+r) < g+y
                for g, y, r in signals
            ):
                return t

        k += 1
            
