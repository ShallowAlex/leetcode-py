# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        pre = ListNode(0)
        pre.next = head
        p = pre
        p1 = p
        if m == 0:
            return
        while m > 1:
            p = p.next
            m -= 1
            n -= 1
        p1 = p.next
        p2 = p1.next
        end = p1
        while n > 1:
            node = p1
            p1 = p2
            p2 = p2.next
            p1.next = node
            n -= 1
        p.next = p1
        end.next = p2
        return pre.next