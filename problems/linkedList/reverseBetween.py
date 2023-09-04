def reverseBetween(head, left, right):
    if head == None or head.next == None or left == right:
        return head
    count, current, prev = 1, head, None
    while current:
        if count == left:
            newCurrent = current
            hold = None
            while newCurrent and count <= right:
                next = newCurrent.next
                newCurrent.next = hold
                hold = newCurrent
                newCurrent = next
                count += 1
            if prev: 
                prev.next = hold
            else:
                head = hold
            current.next = newCurrent
            return head
        count+=1
        prev = current
        current = current.next
    return head
        