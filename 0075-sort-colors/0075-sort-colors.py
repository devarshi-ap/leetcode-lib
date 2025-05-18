class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # naive: count # 0s/1s/2s in. hashtable, then overwrite while decrementing held-count
        count = {0: 0, 1: 0, 2: 0}
        for x in nums:
            count[x] = 0 if x not in count else count[x] + 1
        
        color = 0
        idx = 0
        while color < 3:
            if count[color] != 0:
                count[color] -= 1
                nums[idx] = color
                idx += 1
            else:
                color += 1

            

