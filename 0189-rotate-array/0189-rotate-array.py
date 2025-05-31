class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        rotated = [0]*N

        for i in range(N):
            rotated[(i + k) % N] = nums[i]

        for i in range(len(rotated)):
            nums[i] = rotated[i]