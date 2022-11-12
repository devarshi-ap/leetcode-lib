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
    
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        sum = 0
        curr = head
        idx = self.get_length(head)
        
        while idx != 0:
            idx -= 1
            sum += curr.val * pow(2, idx)
            curr = curr.next
        
        return sum
            
        