import sys
from queue import Queue

n=int(sys.stdin.readline())

cnt=0
while cnt<n:
    data, idx= map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().split()))

    q=Queue()

    for i,p in enumerate(priority):
        q.put((i,p))

    index=0
    state=True
    while state:
        i, p= q.get()
        if any(p<i[1] for i in q.queue):
            q.put((i,p))
        else:
            index+=1
            if i== idx:
                print(index)
                state=False

    cnt+=1
