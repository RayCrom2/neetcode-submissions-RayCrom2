class Solution:
    def calculateArea(self, h1, h2, width) -> int:
        return min(h1, h2) * width
    def maxArea(self, heights: List[int]) -> int:
        h1 = 0
        h2 = len(heights) - 1
        result = float('-inf')
        while h1 < h2:
            area = self.calculateArea(heights[h1], heights[h2], h2 - h1)
            result = max(result, area)
            if heights[h1] > heights[h2]:
                h2 -= 1
            else:
                h1 += 1
        return result