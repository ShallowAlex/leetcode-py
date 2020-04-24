# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if len(lists) == 0:
            return None
        def merge2lists(list1, list2):
            head = ListNode(-1)
            p = head
            if not list1:
                return list2
            if not list2:
                return list1
            while list1 and list2:
                if list1.val <= list2.val:
                    p.next = list1
                    list1 = list1.next
                else:
                    p.next = list2
                    list2 = list2.next
                p = p.next
            if not list2:
                p.next = list1
            if not list1:
                p.next = list2
            return head.next
        while len(lists) > 1:
            lists.append(merge2lists(lists.pop(0),lists.pop(0)))
        return lists[0]