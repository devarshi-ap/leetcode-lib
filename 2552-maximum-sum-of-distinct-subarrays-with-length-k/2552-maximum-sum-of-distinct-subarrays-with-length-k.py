class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        1 5 4 2 9 9 9
        -               {1:1} sum=1 (no max yet)
        - -             {1:1, 5:1} sum=1+5 (no max yet)
        - - -           {1:1, 5:1, 4:1} sum=1+5+4=10 (max b/c window reached k-size)
          - - -         {5:1, 4:1, 2:1} sum=sum+(new-old)=11 (set new max whenever entering element > exiting element)
            - - -       {4:1, 2:1, 9:1} sum=sum+(new-old)=15 (new max bc newEl 9 > exitEL 5)
              - - -     {2:1, 9:2} do nothing since dictSize < 3 (not 3 distinct el's)
        """

        maxSum = 0
        currSum = 0
        start = 0
        state = {}

        for end in range(len(nums)):
            newNum = nums[end]
            oldNum = nums[start]
            currSum += newNum # add new num to sum
            state[newNum] = state.get(newNum, 0) + 1

            if end - start + 1 == k: # window is good
                if len(state) == k: # all nums in window distinct
                    maxSum = max(maxSum, currSum) # update max
            
                currSum -= nums[start] # remove old num from sum
                state[oldNum] -= 1
                if state[oldNum] == 0:
                    del state[oldNum]
                start += 1

        return maxSum
        