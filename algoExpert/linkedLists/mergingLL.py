# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergingLinkedLists(linkedListOne, linkedListTwo):
    l1 = l2 = 0
    curr = linkedListOne
    while curr:
        l1+=1
        curr = curr.next
    curr = linkedListTwo
    while curr:
        l2+=1
        curr = curr.next
    one = linkedListOne
    two = linkedListTwo
    while l1>l2:
        one = one.next
        l1-=1
    while l2>l1:
        two = two.next
        l2-=1
    while one and two:
        if one == two:
            return one
        one = one.next
        two = two.next
        
    return None
