# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        def build(head1, tail):
            if head1 == tail:
                return None
            mid = head1
            p = head1
            while p != tail and p.next != tail:
                mid = mid.next
                p = p.next.next
            if not mid:
                return None
            node = TreeNode(mid.val)
            node.left = build(head1, mid)
            node.right = build(mid.next, tail)
            return node
        return build(head, None)