N=int(input())

mix=[]

for five in range(N):
    for three in range(N):
        if N==five*5+three*3:
            mix.append(five+three)

if mix==[]:
    print(-1)
else:
    print(min(mix))
