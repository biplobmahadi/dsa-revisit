# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeKthNodeFromEnd(head, k):
    prev = None
    curr = head
    second = curr
    while k>0:
        second = second.next
        k-=1
    while second:
        prev = curr
        curr = curr.next
        second = second.next
    if prev:
        prev.next = curr.next
    else:
        head.value = head.next.value
        head.next = head.next.next
