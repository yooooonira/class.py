import sys
n=int(sys.stdin.readline())

info=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    info.append((x,y))


for i in info: #(55, 185)
    count=1
    for j in info: #(55, 185) (58, 183) (88, 186) (60, 175) (46, 155)
        if i[0]<j[0] and i[1] < j[1]:
            count +=1
    print(count, end=" ")
