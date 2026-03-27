class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if head is None or head.next is None:
        raise Exception("List must contain at least two nodes")

    first_head = head
    second_head = head.next

    first_tail = first_head
    second_tail = second_head
    current_node = head.next.next

    add_to_first = True

    while current_node is not None:
        if add_to_first:
            first_tail.next = current_node
            first_tail = current_node
        else:
            second_tail.next = current_node
            second_tail = current_node

        current_node = current_node.next
        add_to_first = not add_to_first

    first_tail.next = None
    second_tail.next = None

    return Context(first_head, second_head)
