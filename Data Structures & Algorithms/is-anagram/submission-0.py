class Solution:
    def compare(self, leftIdx: int, rightIdx: int, length: int) -> bool:
        if length % 2 == 0:
            return leftIdx < rightIdx
        else:
            return leftIdx <= rightIdx
        
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        s_num_occur = defaultdict(int)
        t_num_occur = defaultdict(int)
        leftIdx = 0
        rightIdx = len(s) - 1
        while self.compare(leftIdx, rightIdx, len(s)):
            s_num_occur[s[leftIdx]]  += 1
            t_num_occur[t[leftIdx]]  += 1
            if leftIdx != rightIdx:
                s_num_occur[s[rightIdx]] += 1
                t_num_occur[t[rightIdx]] += 1

            leftIdx += 1
            rightIdx -= 1
        
        print(s_num_occur)
        print(t_num_occur)
        for key in s_num_occur:
            if s_num_occur[key] != t_num_occur[key]:
                return False
            
                
        return True

