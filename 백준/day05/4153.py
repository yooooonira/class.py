while True:
    a,b,c= map(int,input().split())
    x,y,z=sorted([a,b,c]) #입력 순서가 어떻게 들어올지 모르니 정렬 필요
    if x==0 and y==0 and z==0:
        break
    if x**2+y**2==z**2:
        print("right")
    elif x**2+y**2!=z**2:
        print("wrong")
