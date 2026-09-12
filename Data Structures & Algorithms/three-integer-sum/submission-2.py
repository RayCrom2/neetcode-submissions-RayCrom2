class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        prevNum = float('inf')
        for i in range(len(nums) - 2):
            if nums[i] == prevNum:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                currentSum = nums[i] + nums[j] + nums[k]
                if currentSum > 0:
                    k -= 1
                elif currentSum < 0:
                    j += 1
                else:
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
            prevNum = nums[i]
            
        return result