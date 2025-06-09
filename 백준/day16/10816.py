import sys
N=int(sys.stdin.readline())
card1=list(sys.stdin.readline().split())
M=int(sys.stdin.readline())
card2=list(sys.stdin.readline().split())

# for i in range(M):
#     print(card1.count(card2[i]),end=" ")

dic = {}
for i in card1:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in card2:
    if i in dic:
        print(dic[i], end=" ")
    else:
        print(0, end=" ")
