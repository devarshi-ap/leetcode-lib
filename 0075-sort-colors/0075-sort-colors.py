class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # naive: count # 0s/1s/2s in. hashtable, then overwrite while decrementing held-count
        count = {'red': 0, 'white': 0, 'blue': 0}
        for x in nums:
            if x == 0:
                count['red'] += 1
            elif x == 1:
                count['white'] += 1
            else:
                count['blue'] += 1
        
        i = 0
        while count['red'] != 0:
            count['red'] -= 1
            nums[i] = 0
            i += 1
        while count['white'] != 0:
            count['white'] -= 1
            nums[i] = 1
            i += 1
        while count['blue'] != 0:
            count['blue'] -= 1
            nums[i] = 2
            i += 1

            

