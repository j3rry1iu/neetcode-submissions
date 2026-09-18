class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        lpt, rpt = 0, len(numbers) - 1
        stop = len(numbers) // 2 - 1
        while numbers[lpt] + numbers[rpt] != target: 
            if numbers[lpt] + numbers[rpt] > target: 
                rpt -= 1 
            elif numbers[lpt] + numbers[rpt] < target: 
                lpt += 1
        
        return [lpt + 1, rpt + 1]
        

        