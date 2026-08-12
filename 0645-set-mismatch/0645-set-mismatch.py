class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        # In-Place Negative Marking Approach
        """
        index_targets = [0]*len(nums)
        dupe, lost = 0, 0

        for i, x in enumerate(nums):
            if index_targets[x-1] == -1: # already marked
                dupe = x
            else:
                index_targets[x-1] = -1 # mark
        
        for i, x in enumerate(index_targets):
            if x == 0:
                lost = i+1
        
        return [dupe, lost]
        """

        # Math Sum_expected=(n*[n+1])/2
        n = len(nums)
        expectedSum = (n*(n+1)) // 2 # expected sum (formula)
        actualSum = sum(nums) # actual sum
        setSum = sum(set(nums)) # set of nums (without duplicate)

        duplicate = actualSum - setSum
        lost = expectedSum - setSum

        return [duplicate, lost]
        
        
