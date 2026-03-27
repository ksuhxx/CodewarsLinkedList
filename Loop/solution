def loop_size(node):
    slow = node
    fast = node

    while True:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            break

    count = 1
    current = slow.next

    while current != slow:
        count += 1
        current = current.next

    return count
