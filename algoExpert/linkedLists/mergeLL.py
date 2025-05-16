# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def mergeLinkedLists(headOne, headTwo):
    one, two = headOne, headTwo
    main = head = LinkedList(0)
    while one and two:
        if one.value < two.value:
            head.next = one
            one = one.next
        else:
            head.next = two
            two = two.next
        head = head.next
    if one:
        head.next = one
    if two:
        head.next = two
    return main.next
            
