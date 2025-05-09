# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

# I thought about provided solution from algo first (next time do it) - math sum system
def sumOfLinkedLists(linkedListOne, linkedListTwo):
    if not linkedListOne:
        return linkedListTwo
    if not linkedListTwo:
        return linkedListOne
    one = 0
    curr = linkedListOne
    n = 0
    while curr:
        val = curr.value * 10**n
        one = one+val
        curr = curr.next
        n+=1
    two = 0
    curr = linkedListTwo
    n = 0
    while curr:
        val = curr.value * 10**n
        two = two+val
        curr = curr.next
        n+=1
    res = one+two
    if not res:
        return LinkedList(0)
    dummy = LinkedList(None)
    curr = dummy
    while res > 0:
        digit = res % 10
        res = res // 10
        node = LinkedList(digit)
        curr.next = node
        curr = node
    return dummy.next
    