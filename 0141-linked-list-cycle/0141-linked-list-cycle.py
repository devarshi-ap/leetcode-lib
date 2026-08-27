# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # initialize a pointer to the head node
        curr = head
        # use a while loop to advance the pointer through node.next
        while curr is not None:
            print(curr.val)
            if curr.val == "X":
                return True
            curr.val = "X"
            curr = curr.next
        # stop when it reaches None
        print("None")
        return False