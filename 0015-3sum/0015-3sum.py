class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:

        # sort arr, then run TwoPointers within for-loop
        nums.sort()
        combos = []

        for i in range(len(nums)-2): # - 2 saves 2 spaces right of i for L,R
            if i > 0 and nums[i] == nums[i-1]:  # skip duplicate i
                continue
            # now just 2SUM!
            l, r = i+1, len(nums)-1
            while l < r:
                # print(i, l, r)
                c_sum = nums[i] + nums[l] + nums[r]
                if c_sum > 0: # too much (<--R)
                    r -= 1
                elif c_sum < 0: # too little (L-->)
                    l += 1
                else: # perfecto (save combo, move both inward)
                    combos.append([nums[i], nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while l < r and nums[l] == nums[l-1]:  # skip duplicate l
                        l += 1
                    while l < r and nums[r] == nums[r+1]:  # skip duplicate r
                        r -= 1

        return combos