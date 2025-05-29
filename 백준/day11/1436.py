import sys
n=int(sys.stdin.readline())

# end=[]
# for i in range(999999999):
#     if "666" in str(i):
#         end.append(i)
# print(end[n])


cnt=0
num=0
state=True
while state:
    num+=1
    if "666" in str(num):
        cnt+=1
    if n==cnt:
        state=False
print(num)
