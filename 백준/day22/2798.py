import sys
from itertools import combinations #조합을 사용

N, M= map (int, sys.stdin.readline().split())
N_list=list(map(int, sys.stdin.readline().split()))


print(max(list( i for i in map (sum, combinations(N_list,3))if i <= M)))
