from collections import Counter

def solution(array):
#     dic ={}
#     for i in array:
#         dic[i]=dic.get(i,0) +1
    
#     max_count = max(dic.values()) 
    
#     if list(dic.values()).count(max_count)>1:
#         return -1
    
#     return max(dic, key=dic.get)

    counter = Counter(array)
    most=counter.most_common()
    
    if len(most)==1 or most[0][1]>most[1][1]:
        return most[0][0]
    return -1

