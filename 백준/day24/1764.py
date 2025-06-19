import sys

N,M=map(int, sys.stdin.readline().split())

never_seen=set()
never_heard=set()
never_seen_and_heard=set()

for _ in range(N):
    name=sys.stdin.readline().strip()
    never_seen.add(name)
for _ in range(M):  
    name=sys.stdin.readline().strip()
    never_heard.add(name)

never_seen_and_heard=sorted(never_seen & never_heard)

print(len(never_seen_and_heard))
for i in never_seen_and_heard:
    print(i)

#딕셔너리를 쓰게되면 이중루프를 돌게 된다. 
#set의 연산자와 메서드 신기한게 많다.
