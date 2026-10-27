class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        unique = 0
        for idx, num in enumerate(nums):
            
            if num == val:
                nums[idx] += 100000000000000000000000000000000000000
            else:
                unique+=1
        
        nums.sort()

        return unique