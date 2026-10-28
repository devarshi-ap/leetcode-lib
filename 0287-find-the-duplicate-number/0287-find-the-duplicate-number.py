class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        # naive: keep adding to set until duplicate found -> O(n) time & space
        # optimized: do in-place Floyd's with 2 ptrs; phase 1 detects cycle, phase 2 finds entrance of cycle

        # Phase 1: Find the intersection point in the cycle
        slow = fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        
        # print(">", slow, fast)

        # Phase 2: Find Entrance to cycle (reset fast, and now move both ptrs 1 step at a time until converging at entrance)
        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow
