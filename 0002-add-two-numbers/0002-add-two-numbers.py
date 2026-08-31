# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = head = ListNode(0)
        c = 0

        while l1 or l2 or c:
            # read l1/l2 val if possible
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # get sum, new_digit, carry
            total = val1 + val2 + c
            new_digit = total % 10
            c = total // 10

            print(f"{val1}+{val2}={total}\t({c} | {new_digit})")
            
            # new node
            dummy.next = ListNode(new_digit)
            
            # move only if possible
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            dummy = dummy.next

        return head.next