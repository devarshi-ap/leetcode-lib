# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """ Naive (destructive mutation) Approach:
        a. init pointer to head node (c=head)
        In while loop
            b. change the node's value to some marker (c.val="X")
            c. advance pointer (c=c.next)
        """
        if head is None:
            return False
        
        s = f = head

        while f and f.next is not None:
            print(s.val, f.val)
            s = s.next
            f = f.next.next
            if f == s:
                return True
        # stop when it reaches None
        print("None")
        return False