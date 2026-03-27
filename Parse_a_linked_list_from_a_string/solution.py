class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

def linked_list_from_string(list_repr: str):
    if list_repr == "None":
        return None

    values = list_repr.split(" -> ")[:-1]
    head = Node(int(values[0]))
    current = head

    for value in values[1:]:
        current.next = Node(int(value))
        current = current.next

    return head
