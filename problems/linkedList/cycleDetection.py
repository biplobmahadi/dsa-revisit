def cycleDetection(head):
    map = {}
    current = head
    while current:
        if not map.get(current):
            map[current] = True
            current = current.next
        else:
            return current
    return None

def cycleDetectionOptimal(head):
    if head == None:
        return None
    hare = tortoise = head
    count = 0
    while (hare and hare != tortoise) or count < 1:
        if count<1:
            count+=1
        tortoise = tortoise.next
        if hare.next:
            hare = hare.next.next
        else:
            hare = None
    if hare:
        begin = head
        while begin != hare:
            begin = begin.next
            hare = hare.next
        return hare
    return None
