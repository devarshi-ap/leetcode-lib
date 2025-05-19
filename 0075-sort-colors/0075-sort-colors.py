class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        """
        # naive: count # 0s/1s/2s in. hashtable, then overwrite while decrementing held-count (O(n))
        # naive suffices here as it's just a simple in-place sorting question

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
        """

        red, insptr, blue = 0, 0, len(nums)-1
        while insptr <= blue: # while inspector is not done inspecting all nums
            if nums[insptr] == 0: # inspector found 0
                # [pass/swap to red] & [move red up (to an unknown)]
                nums[red], nums[insptr] = nums[insptr], nums[red]
                insptr += 1
                red += 1
            elif nums[insptr] == 1: # inspector found 1
                # desired! inspector inspect next number
                insptr += 1
            else: # inspector found 2
                # [pass/swap to blue] & [move blue down (to an unknown)]
                nums[blue], nums[insptr] = nums[insptr], nums[blue]
                blue -= 1

