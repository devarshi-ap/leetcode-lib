# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Naive Sol'n = pointer walk + stack (FILO)
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
        """

        # Optimized Sol'n = 3-ptr walk (prev/curr/next) and flip as you go
        prev = None
        curr = head
        
        while curr:
            nxt = curr.next # save next node
            curr.next = prev # flip link
            # shift ptr's
            prev = curr
            curr = nxt
        
        return prev