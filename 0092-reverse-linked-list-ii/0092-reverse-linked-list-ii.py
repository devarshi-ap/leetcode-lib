# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        l = r = dummy = head
        stack = []

        # pointer walk and add to stack
        counter = 1
        while r:
            if left <= counter <= right:
                stack.append(r.val)
                print(f"added {r.val} to stack: {stack}")
            counter += 1
            r = r.next
        
        # second pointer walk and update node value using item popped from stack
        counter = 1
        while l:
            if left <= counter <= right:
                l.val = stack.pop()
                print(f"updated value to {l.val}")
            counter += 1
            l = l.next

        return dummy
            


