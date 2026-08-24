class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 2ptr's from opposite ends, calc area, track max, move ptr with smaller height inward (stop when l=r)
        l, r = 0, len(height)-1
        maxA = 0

        while l < r:
            currA = (r - l) * min(height[l], height[r]) # area = w * h
            maxA = max(maxA, currA)
            print(f"{height[l]}, {height[r]}, {currA}, {maxA}")
            if height[l] <= height[r]: # l same or smaller, move inward
                l += 1
            else:
                r -= 1
        
        return maxA