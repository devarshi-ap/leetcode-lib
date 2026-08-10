class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        left, right = 0, n
        for i in range(n):
            ans.extend([nums[left], nums[right]])
            left += 1
            right += 1
        
        return ans