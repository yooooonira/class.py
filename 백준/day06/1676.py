import math

n = int(input())
result=math.factorial(n)

result=str(result)
idx=[] #뒤부터 처음 0이 아닌 인덱스가 필요
for i in range(len(result)-1,-1,-1):
    if result[i]!="0":
        idx.append(i) 
        break 

cnt= result[idx[0]:].count("0")
print(cnt)
