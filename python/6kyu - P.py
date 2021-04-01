class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def insert_nth(head, index, data):
    newNode = Node(data)
    print(head, index, data)

    if index == 0:
        newNode.next = head
        return newNode

    idx = 0
    currentNode = head
    while idx < index - 1:
        idx = idx + 1
        currentNode = currentNode.next

        if currentNode.next is None:
            if index - idx == 1:
                newNode.next = currentNode.next
                currentNode.next = newNode
                return head
            else:
                raise IndexError('End of the list!')

    newNode.next = currentNode.next
    currentNode.next = newNode

    return head
