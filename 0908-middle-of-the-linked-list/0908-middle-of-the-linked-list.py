# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """ Naive: ptr A iterates through LL and once done, echoe's back how many steps. ptr B then takes 1/2 as many steps to get to middle.

        pA = pB = head
        steps = 0

        while pA.next is not None:
            print(pA.val)
            pA = pA.next
            steps += 1
        
        halfSteps = (steps + 1) // 2
        for i in range(halfSteps):
            pB = pB.next
        
        return pB
        """

        # Can also use Two-Pointers (fast/slow; always guarantees slow is half way to fast; stop when fast == None)
        s = f = head
        while f and f.next is not None:
            s = s.next
            f = f.next.next
        return s