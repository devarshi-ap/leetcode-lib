class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # get Left-hand products, then Right-hand, then zipper merge

        ans = []
        left = []
        right = []

        # get Left-hand products
        product = 1
        for i,x in enumerate(nums):
            left.append(product)
            product *= x
        
        # get Right-hand products (same method, just read nums backwards)
        product = 1
        for i in range(len(nums)-1, -1, -1):
            right.append(product)
            product *= nums[i]
        right = list(reversed(right))
    
        # zipper merge
        for i in range(len(left)):
            ans.append(left[i] * right[i])
        
        return ans
            

        """
        [1, 2, 3, 4] -> L = [1*, 1, 2, 6]
                     -> R = [24, 12, 4, 1*]
                     -> ans = [24, 12, 8, 6]
        """