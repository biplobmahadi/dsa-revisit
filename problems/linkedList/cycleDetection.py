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