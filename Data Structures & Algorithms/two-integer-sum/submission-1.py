class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            to_find = target - num
            if to_find in d:
                return [d[to_find], i]
            d[num] = i
        return []