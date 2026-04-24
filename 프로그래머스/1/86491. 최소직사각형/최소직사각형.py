def solution(sizes):
    max_w = 0
    max_h = 0
    
    for w, h in sizes:
        w, h = max(w, h), min(w, h) 
        max_w = max(max_w, w)
        max_h = max(max_h, h)
    
    return max_w * max_h
# 명함은 회전이 가능함 -> (w,h), (h,w) 모두 가능 
# 어떤 명함은 가로가 길고, 어떤 명함은 세로가 길면 전체 크기를 정할때 기준이 깨짐 
# 그래서 가로로 기준을 잡음  line6
