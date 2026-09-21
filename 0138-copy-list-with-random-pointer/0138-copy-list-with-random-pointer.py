"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head: return None

        # first pass: record {oldNode a -> newNode A} mappings
        nodeMap = {}
        curr = head
        while curr:
            nodeMap[curr] = Node(x=curr.val)
            curr = curr.next

        # second pass: assigning .next/.random to newNodes
        for oldNode in nodeMap:
            newNode = nodeMap[oldNode]
            newNode.next = nodeMap[oldNode.next] if oldNode.next else None
            newNode.random = nodeMap[oldNode.random] if oldNode.random else None

        return nodeMap[head]
