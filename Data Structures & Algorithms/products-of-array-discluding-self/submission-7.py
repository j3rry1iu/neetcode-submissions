class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        newList = []
        product = 1
        prod = 1
        count = 0
        for num in nums: 
            product *= num
            if num == 0: 
                count += 1
        if count > 1: 
            newList = [0] * len(nums)
        elif count == 1: 
            for num in nums: 
                if num != 0: 
                    prod *= num
            for i in range(len(nums)):
                if nums[i] == 0: 
                    newList.append(prod)
                else: 
                    newList.append(0)
        else:
            for i in range(len(nums)):
                newList.append(product//nums[i])
        return newList


        