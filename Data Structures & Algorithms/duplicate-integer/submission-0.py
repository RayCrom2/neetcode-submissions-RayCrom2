class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if nums:
            seen = {nums[0]}
        for i in range(1, len(nums)):
            if nums[i] in seen:
                return True
            else:
                seen.add(nums[i])
        return False