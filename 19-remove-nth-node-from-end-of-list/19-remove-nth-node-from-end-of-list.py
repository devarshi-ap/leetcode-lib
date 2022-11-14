# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    
    def get_length(self, head):
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        return count

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        nth = self.get_length(head) - n
        
        curr = head
        temp = curr
        prev = None

        if nth == 0:
            head = curr.next
            return head

        while curr.next and nth > 0:
            nth -= 1
            prev = curr
            curr = curr.next
        
        prev.next = curr.next
        curr = None
        return temp
        
        