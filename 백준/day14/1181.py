import sys

n=int(sys.stdin.readline())
data = data = [sys.stdin.readline().strip() for _ in range(n)]
sorted_data=sorted(set(data), key= lambda x : (len(x), x))

for i in sorted_data:
    print(i)
