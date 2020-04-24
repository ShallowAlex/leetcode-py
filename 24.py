# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        q = ListNode(-1)
        q.next = head
        tmp = q
        while head and head.next:
            p1 = head
            p2 = head.next

            tmp.next = p2
            p1.next = p2.next
            p2.next = p1

            head = p1.next
            tmp = p1
        return q.next