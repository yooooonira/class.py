import math
def solution(numer1, denom1, numer2, denom2):
    x=(numer1*denom2)+(numer2*denom1)
    y=denom1*denom2
    
    g=math.gcd(x,y)
    x//=g
    y//=g
            
    return [x,y]
    
    # return [x//g, y//g]

# 1. denom끼리 같은 숫자인지 확인한다. 
# 2. 같은 숫자면 
#   2-1. 더한다. 
# 3. 같은 숫자가 아니면 
#   2-2. denom에는 서로를 곱하고, numer은 상대의 denom을 곱한다.
# 4. [x,y] 형태에서 약분을 한다. 
#  for i in range(y)로 x를 나눌수있으면 나눈다. 

# 2번, 3번 -> 분모가 같은 경우도 같은 연산으로 처리 가능하니까 비교문쓰지 않아도 된다.
# 4번 -> gcd