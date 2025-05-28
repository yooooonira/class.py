num = int(input())
for i in range(num):
    text=input()
    count=[0] *len(text)
    total=0
    for i in range(len(text)):
        if text[i] =="O":
            if i==0:
                count[i]=1
            else:
                count[i]=count[i-1]+1 #누적 값을 여기서
        # if text[i] =="O":
        #     count[i] += 1
        #     count[i+1] = count[i] 
        #이렇게 하면 마지막 인데스에서 IndexError
        else:
            count[i]=0
    for i in range(len(count)):
        total+=count[i]
    print(total)
