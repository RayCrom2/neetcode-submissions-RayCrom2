class Solution:
    def trap(self, height: List[int]) -> int:
        maxL = height[0]
        maxR = height[len(height) - 1]
        left = 1
        right = len(height) - 2
        result = 0

        while left <= right:
            if maxL < maxR:
                difference = maxL - height[left]
                result += difference if difference > 0 else 0
                if height[left] > maxL:
                    maxL = height[left]
                left += 1
            else:
                difference = maxR - height[right]
                result += difference if difference > 0 else 0
                if height[right] > maxR:
                    maxR = height[right]
                right -= 1
                
        return result
        '''
        height 1: 0 //track
        height 2: 2 // >= 0, calculate area, track
        height 3: 0 //count += 0
        height 4: 3 // >= 2 so calculate area = min(3,2) * i - prev - count; track
        height 5: 1
        '''