import sys

K, N = map(int, sys.stdin.readline().split())

length=[int(sys.stdin.readline()) for i in range(K)]

start=1 
max_length = max(length)

while(start <= max_length):
  mid = (start + max_length) // 2
  cnt = 0

  for i in length:
    cnt += i // mid
    
  if cnt >= N:
    start = mid + 1
  else:
    max_length = mid - 1

print(max_length)
