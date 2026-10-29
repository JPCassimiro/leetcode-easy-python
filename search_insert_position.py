class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        for idx, num in enumerate(nums):
            if num == target:
                return idx
        
        for idx, num in enumerate(nums):
            if num > target:
                return idx
        
        return len(nums)