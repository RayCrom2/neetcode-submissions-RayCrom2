class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        product = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = product
            product *= nums[i]
        product = nums[-1]
        #second param is excluded from loop
        for j in range (len(nums) - 2, -1, -1): 
            suffix[j] = product
            product *= nums[j]

        return [a * b for a, b in zip(prefix, suffix)]
        
