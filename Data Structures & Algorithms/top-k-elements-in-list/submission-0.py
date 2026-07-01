class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        frequencies = [[] for i in range(len(nums) + 1)]       
        for i in nums:
            count[i] = 1 + count.get(i, 0)

        for key, value in count.items():
            frequencies[value].append(key)

        result = []
        for i in range(len(frequencies) - 1, 0, -1):
            for num in frequencies[i]:
                result.append(num)
                if len(result) == k:
                    return result

