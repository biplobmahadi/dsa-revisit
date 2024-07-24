def floydsHareAndTortoiseMiddle(head):
    slow, fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow # it will return the middle

def floydsHareAndTortoiseCycle(head):
    slow, fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False # it will return is cycle or not
