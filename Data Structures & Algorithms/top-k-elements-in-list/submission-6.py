class Solution:
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newNum = []
        numsCount = dict(Counter(nums))
        sortNums = dict(sorted(numsCount.items(), key=lambda item: item[1], reverse=True))
        sortedList = list(sortNums.keys()) 
        for i in range(k): 
            newNum.append(sortedList[i])
        return newNum



        
        