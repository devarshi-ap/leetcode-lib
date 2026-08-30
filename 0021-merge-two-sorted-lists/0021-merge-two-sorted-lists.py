# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # if either list is empty, return the other
        if not list1: return list2
        if not list2: return list1
        
        ans = ListNode(0)
        dummy = ans

        while list1 and list2:
            if list1.val < list2.val: # L1 smaller (add then move L1)
                dummy.next = list1
                list1 = list1.next
            else: # L1 equal or bigger (add L2 and move)
                dummy.next = list2
                list2 = list2.next
            dummy = dummy.next
        
        # while loop only runs until either list != None (now check both cases)
        if list1 is None:    # L1 finished, add rest of L2
            dummy.next = list2
        else: # L2 finished, add rest of L1
            dummy.next = list1
        
        return ans.next
        



