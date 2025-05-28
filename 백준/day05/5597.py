import sys

submitted = []
for i in range(28):
	submitted.append(int(sys.stdin.readline()))

all =[]
for i in range(1,31):
	all.append(i)


# for i in all: 
# 	if i in submitted:
# 		del all[i-1]  # for문을 돌면서 del하니까 인덱스가 바뀜 -> indexerror

result=[i for i in all if i not in submitted]

print(*result, sep="\n")
