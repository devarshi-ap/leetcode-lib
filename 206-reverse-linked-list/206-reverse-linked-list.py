# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        
        nodes = []
        
        while head:
            nodes.append(head)
            head = head.next
        
        head = temp = nodes.pop()
        
        while len(nodes)>0:
            temp.next = nodes.pop()
            temp = temp.next      
        
        temp.next = None
        return head
            
        