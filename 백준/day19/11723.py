from collections import deque
import sys
N=int(sys.stdin.readline())
s=set()
for _ in range(N):
    command=list(sys.stdin.readline().split())
    if command[0]=="add":
        s.add(int(command[1]))      
    elif command[0]=="remove":
            s.discard(int(command[1]))
    elif command[0]=="check":
        if int(command[1]) in s:
            print(1)
        else:
            print(0)
    elif command[0]=="toggle":
        if int(command[1]) in s:
            s.remove(int(command[1]))
        else:
            s.add(int(command[1])) 
    elif command[0]=="all":
        s.update(set(range(1,21)))
    elif command[0]=="empty":
        s.clear()
