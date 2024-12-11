from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 and not list2: return None
        head = ListNode()
        newList = head
        while list1 and list2:
            if list1.val > list2.val:
                newList.next = list2
                list2 = list2.next
            else:
                newList.next = list1
                list1 = list1.next
            newList = newList.next
        if list1:
            newList.next = list1
        if list2:
            newList.next = list2
        return head.next
