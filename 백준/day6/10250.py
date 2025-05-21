idx=int(input()) #몇 번 돌건지
for i in range(idx):
    h,w,n= map(int,input().split())

    #층수
    y=n%h
    if y==0:
        y=h #꼭대기층 

        

    for i in range(w,0,-1):
        if n<=i*h:
            x=i



    print(f"{y}{x:02d}")
