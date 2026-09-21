from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        maxLength = 1
        left = 0
        seen = defaultdict(int)
        seen[s[left]] = 1
        for i in range(1, len(s)):
            key = s[i]
            if seen[key] == 1:
                while s[left] != key:
                    seen[s[left]] = 0                        
                    left += 1
                left += 1
            else:
                seen[key] = 1
                maxLength = max(maxLength, i - left + 1)
        return maxLength

'''
if length of string is 0
return 0
maxLength = 1
left = 0
dict = defaultdict(int)
dict[s[left]] = 1

for i in [1, len(s)):
    key = s[i]
    if dict[key] = 1:
        while s[left] != key:
            dict[s[left]] = 0
            left += 1
        left += 1
    else:
        s
        maxLength = max(maxLength, i - left + 1)
return maxLength
'''