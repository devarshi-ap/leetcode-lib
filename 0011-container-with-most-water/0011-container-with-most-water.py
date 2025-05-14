class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, maxArea = 0, len(height)-1, 0
        while left < right:
            currArea = (right - left) * (min(height[right], height[left]))
            maxArea = max(maxArea, currArea)
            if height[left] > height[right]:
                # L-line taller than R-line, move R in
                right -= 1
            else:
                # R-line taller (or equal to; same difference) than L-line, move L in
                left += 1
        return maxArea