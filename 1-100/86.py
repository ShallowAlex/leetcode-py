# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     def partition(self, head: ListNode, x: int) -> ListNode:
#         head1 = ListNode(-1)
#         head2 = ListNode(-1)
#         p1 = head1
#         p2 = head2
#         while head:
#             if head.val < x:
#                 head1.next = head
#                 head1 = head1.next
#             else:
#                 head2.next = head
#                 head2 = head2.next
#             head = head.next
#         head2.next = None
#         head1.next = p2.next
#         return p1.next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        leftDummy = ListNode(None)
        rightDummy = ListNode(None)
        
        left = leftDummy
        right = rightDummy
        
        while head:
            if head.val < x:
                left.next = head
                left = head
            else:
                right.next = head
                right = head
            head = head.next
        
        left.next = rightDummy.next
        right.next = None
        return leftDummy.next