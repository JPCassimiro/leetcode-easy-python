class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        _map = {}
        
        for idx, num in enumerate(nums):
            print(target - num)
            if _map.get(num) is not None:
                return [idx, _map[num]]
            _map[target - num] = idx               

        
        