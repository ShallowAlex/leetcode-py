# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next:
            return head
        tail = head
        n = 1
        while tail.next:
            tail = tail.next
            n += 1
        tail.next = head
        k = k % n
        for i in range(n-k):
            tail = tail.next
        new_head = tail.next
        tail.next = None
        return new_head