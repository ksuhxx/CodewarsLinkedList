class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def swap_pairs(head):
    if head is None or head.next is None:
        return head

    new_head = head.next
    prev = None
    current = head

    while current and current.next:
        first = current
        second = current.next

        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        current = first.next

    return new_head
