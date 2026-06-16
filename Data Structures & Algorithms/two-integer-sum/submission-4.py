class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = {}
        for i, n in enumerate(nums):
            diff[target - n] = i
        for i, n in enumerate(nums):
            if n in diff and diff[n] != i:
                return [i, diff[n]]
        return []
