class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def removeDuplicatesFromLinkedList(linkedList):
    if not linkedList: return None
    prev = linkedList
    curr = linkedList.next
    while curr:
        if prev.value == curr.value:
            prev.next = curr.next
            curr = curr.next
        else:
            prev = curr
            curr = curr.next
    return linkedList
