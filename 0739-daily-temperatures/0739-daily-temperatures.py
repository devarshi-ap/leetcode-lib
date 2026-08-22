class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # "next warmer temp" == Monotonic Decreasing Stack (act on x>stack[-1])
        days = [0 for x in temperatures] # all 0 to begin
        stack = []

        for i, temp in enumerate(temperatures):
            print(i, temp)
            while stack and temp > temperatures[stack[-1]]:
                prev_temp_i = stack.pop()
                days[prev_temp_i] = i - prev_temp_i
            stack.append(i)
        return days