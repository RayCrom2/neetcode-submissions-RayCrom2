class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        seen = {val: 1 for val in nums}
    
        for key in seen.keys():
            if (key + 1) in seen and (key - 1) not in seen:
                i = 2
                seen[key] += 1
                while key + i in seen:
                    seen[key] += 1
                    i += 1

        # print(seen)
        return max(seen.values())
'''
        see 2
        look for 2 - 1
        doesnt exist

        look for 2 + 1
        exists
        1 = 1 + 1
        seen[2] = 2
        seen[3] = seen[2]

        2: 2
        3: 2

        see 20
        look for 20 - 1
        doesnt exist

        look for 20 + 1
        doesnt exist
        
        see 4
        look for 4 - 1
        exists
        seen[4] = seen[4] + seen[4 - seen[3]]
        seen[4] = seen[4] + seen[2]
        seen[4] = 1 + 2
        seen[4] = 3
        seen[2] = 3

        look for 4 + 1
        exists
        seen[]

        seen[key] = seen[key] + (seen[key + 1] or seen[key + seen[key + 1]]
        seen[key + seen[key + 1]] = seen[key]

'''