class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        index_targets = [0]*len(nums)
        dupe, lost = 0, 0

        for x in nums:
            idx = x-1
            if index_targets[idx] == -1: # already marked
                dupe = x
            else:
                index_targets[idx] = -1 # mark
        
        print(index_targets)
        for i, x in enumerate(index_targets):
            print(x, i)
            if x == 0:
                lost = i+1
        
        return [dupe, lost]
            
