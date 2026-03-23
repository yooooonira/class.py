from collections import defaultdict

class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        # n=len(hours)
        # for i in range(n):
        #     hours[i]%=24 #배열 재정의
        # count=0

        # for i in range(n):
        #     for j in range(i+1,n):
        #         if (hours[i]+hours[j])%24==0:
        #             count +=1
        # return count 

        count = 0
        freq = defaultdict(int)  # 나머지 개수 저장
        
        for i in hours: # 12, 12, 30, 24, 24
            r = i % 24 # 나머지값 저장 
            need = (24 - r) % 24 
            
            count += freq[need]
            freq[r] += 1
        
        return count

