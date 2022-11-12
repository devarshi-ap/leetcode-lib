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
    
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        
        mid = len(nodes) / 2
        return nodes[mid]
        