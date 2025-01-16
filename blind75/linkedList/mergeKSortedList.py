# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def merge(list1, list2):
    head = tail = ListNode() 
    while list1 and list2:
        if list2.val >= list1.val:
            tail.next = list1
            list1 = list1.next
        else:
            tail.next = list2
            list2 = list2.next
        tail = tail.next
        
    if list1:
        tail.next = list1
    if list2:
        tail.next = list2
    return head.next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists: return None
        while len(lists) > 1:
            newLists = []
            for i in range(0, len(lists), 2):
                first = lists[i]
                second = lists[i+1] if i+1 < len(lists) else None
                merged = merge(first, second)
                newLists.append(merged)
            lists = newLists
        
        return lists[0]
