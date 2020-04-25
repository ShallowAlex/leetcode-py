# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
#栈理解容易，尾插麻烦
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0) #感觉在学英语
        dummy.next = head
        pre = dummy
        tail = dummy
        while 1:
            n = k
            while n and tail:
                tail = tail.next
                n -= 1
            #剩余节点不足k则退出循环
            if not tail:
                break
            head = pre.next #定位即将尾插后的第一个前置节点
            #进行尾插循环
            while pre.next != tail:
                tmp = pre.next
                pre.next = tmp.next #断开了tmp的链接
                tmp.next = tail.next # tmp接上tail后
                tail.next = tmp #接上tail后tmp
            pre = head
            tail = head
        return dummy.next