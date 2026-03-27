def stringify(node):
    result = ""

    while node is not None:
        result += str(node.data) + " -> "
        node = node.next

    result += "None"
    return result
