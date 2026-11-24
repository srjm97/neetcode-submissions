class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        n = len(nums)
        ans = []
        for i in range(n):
            to_find = target - nums[i]
            pos = d.get(to_find)
            if not isinstance(pos, int):
                d[nums[i]] = i
                continue
            ans = [pos,i]
        return ans