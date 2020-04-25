# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        prehead = ListNode(-1)
        prehead.next = head
        pre = prehead
        cur = prehead
        while cur:
            cur = cur.next
            
            while cur and cur.next and cur.val == cur.next.val:
                value = cur.val
                cur = cur.next
                while cur and cur.val == value:
                    cur = cur.next
            pre.next = cur
            pre = pre.next

        return prehead.next