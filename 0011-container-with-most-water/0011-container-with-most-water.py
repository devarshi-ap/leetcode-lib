class Solution:
    def maxArea(self, height: List[int]) -> int:
        # naive: nested for-loop calculate & compare maxArea O(n^2)
        # 1. init pointers
        left, right = 0, len(height)-1
        maxArea = 0

        # 2. setup algo invariant
        while left < right:
            # 3. do calculations
            currArea = (right-left)*(min(height[left], height[right]))
            maxArea = max(maxArea, currArea)
            #. 4. move pointer(s) accordingly
            if (height[left] > height[right]):
                # L-height > R-height
                right -= 1
            else:
                # L-height > R-height
                # L-height = R-height
                left += 1
        
        return maxArea