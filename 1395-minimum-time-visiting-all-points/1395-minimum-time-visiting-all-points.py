class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        # running sum of time with a coord-pair walk (A->B + B->C + ...)
        # time b/n A-B = max(x-coord diff, y-coord diff)
        time = 0
        for i in range(1, len(points)):
            x_diff = abs(points[i][0] - points[i-1][0]) # |x2 - x1|
            y_diff = abs(points[i][1] - points[i-1][1]) # |y2 - y1|
            time += max(x_diff, y_diff)
        
        return time
