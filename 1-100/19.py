# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        #题目中保证给定的 n 是有效的。(同时n是大于0的)
        p1 = head
        p2 = head
        for _ in range(n):
            p1 = p1.next
        if not p1:
            return head.next
        while p1.next:
            p1 = p1.next
            p2 = p2.next
        p2.next = p2.next.next
        return head