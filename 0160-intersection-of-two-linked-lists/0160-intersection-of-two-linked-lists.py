# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        # same trick as (141. LL Cycle): fast/slow ptrs that will merge on point of intersection
        
        pA, pB = headA, headB

        while pA != pB:
            # print(f"A={headA.val}, B={headB.val}")
            pA = pA.next if pA else headB
            pB = pB.next if pB else headA
        
        return pA