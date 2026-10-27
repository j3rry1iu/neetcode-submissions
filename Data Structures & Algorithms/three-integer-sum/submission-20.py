class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort() 
        ans = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue 
            target = 0 - nums[i]
            lptr = i + 1 
            rptr = len(nums) - 1
            while lptr < rptr:
                if nums[lptr] + nums[rptr] == target: 
                    ans.append([nums[i], nums[lptr], nums[rptr]])
                    rptr -= 1
                    lptr += 1
                    while lptr < rptr and nums[lptr] == nums[lptr - 1]:
                        lptr += 1
                    while lptr < rptr and nums[rptr] == nums[rptr + 1]:
                        rptr -= 1
                elif nums[lptr] + nums[rptr] > target: 
                    rptr -= 1
                elif nums[lptr] + nums[rptr] < target:
                    lptr += 1
            
        return ans
                

            
             



        