class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = defaultdict(int)
        for i in range(len(nums)):
            diff[target - nums[i]] = i
        for i in range(len(nums)):
            if nums[i] in diff and diff[nums[i]] != i:
                return [i, diff[nums[i]]]
        return []
