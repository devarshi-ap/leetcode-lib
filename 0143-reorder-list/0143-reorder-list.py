# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode | None) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        stack = []
        
        # first pointer walk records all nodes in order
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        # 2ptr's from opposite ends to reorder
        l, r = 0, len(stack) - 1
        while l < r:
            stack[l].next = stack[r] # l -> r
            l += 1 # move l in

            if l >= r:
                break

            stack[r].next = stack[l] # r -> l+1
            r -= 1 # move r in
        
        stack[l].next = None # Terminate the tail to avoid cycles

        return head

