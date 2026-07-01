class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            char_encoding = [0] * 26

            for char in word:
                char_encoding[ord(char) - ord('a')] += 1
            key = tuple(char_encoding)
            if key not in groups:
                groups[key] = []
            groups[key].append(word)

        return list(groups.values())