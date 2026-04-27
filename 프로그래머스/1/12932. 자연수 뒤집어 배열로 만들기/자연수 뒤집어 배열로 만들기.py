def solution(n):
    # n=str(n) #"12345"
    # n=sorted(n,reverse=True) #["5","4","3","2","1"]
    # n=map(int,n)
    # return list(n)
    
    # return list(map(int, sorted(str(n), reverse=True)))
    
    # return [int(i) for i in sorted(str(n), reverse=True)]

    return list(map(int, reversed(str(n))))