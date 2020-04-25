# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        tmp = []
        p = ListNode(-1)
        q = p
        p.next = head
        while head:
            if head.val in tmp:
                p.next = head.next
                head = head.next
                
            else:
                tmp.append(head.val)
                p = p.next
                head = head.next
        return q.next