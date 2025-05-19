num=int(input()) #10
if num==0:
    print(1)
else:
    for i in range(num-1,0,-1): #9~1
        num*=i

    print(num)
