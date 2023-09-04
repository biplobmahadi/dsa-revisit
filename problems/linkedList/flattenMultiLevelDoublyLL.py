def flatten(head):
    current = head
    while current:
        if current.child:
            newCurrent = current.child
            while newCurrent.next:
                newCurrent = newCurrent.next
            if current.next:
                newCurrent.next = current.next
                current.next.prev = newCurrent
            current.next = current.child
            current.child.prev = current
            current.child = None
        current = current.next
    
    return head