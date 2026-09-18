class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sortedNum = sorted(set(nums))
        countList = [0]
        count = 1
        if nums == []: 
            return 0
        for i in range(1, len(sortedNum)): 
            if sortedNum[i] == sortedNum[i-1] + 1:
                count += 1
            else: 
                countList.append(count)
                count = 1
        countList.append(count)
        return max(countList) 

        