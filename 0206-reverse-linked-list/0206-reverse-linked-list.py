# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # pointer walk + stack (FILO)
        stack = []
        ansHead = dummy = ListNode(0)

        while head:
            stack.append(head.val)
            head = head.next
            # print(stack)
        
        while len(stack) > 0:
            dummy.next = ListNode(stack.pop())
            dummy = dummy.next
        
        return ansHead.next