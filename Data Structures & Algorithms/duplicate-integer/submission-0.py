class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        s = set()
        for num in nums:
            s.add(num)
        if len(nums) != len(s):
            return True
        return False