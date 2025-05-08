# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def reverseLinkedList(head):
    hold = None
    curr = head
    while curr:
        currNxt = curr.next
        curr.next = hold
        hold = curr
        curr = currNxt
    return hold