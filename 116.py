"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        p = root
        head = root
        while p.left:
            if p.left:
                p.left.next = p.right
                if p.next:
                    p.right.next = p.next.left
                    p = p.next
                else:
                    head = head.left
                    p = head
        return root
