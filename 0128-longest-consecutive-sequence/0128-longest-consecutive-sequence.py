class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        # use Set to find sequence starting points & count consecutive nums (track max)
        
        numSet = set(nums)
        maxStreak = 0
        
        # iteration X: is X-1 in set? if yes, X isn't starting point, skip (will read X when you count up from X-1). if no, X is starting point, count up (checking if in set) and track max

        for x in numSet:
            if x-1 not in numSet:
                # X is seq starting pt (start streak, count up)
                streak = 1
                while x+1 in numSet:
                    streak += 1
                    x += 1
                maxStreak = max(streak, maxStreak)
            else:
                # X is NOT seq starting pt (skip; since X gets read anyways when counting up from X-1)
                pass

        return maxStreak