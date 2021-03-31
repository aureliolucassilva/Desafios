# Link -> https://www.codewars.com/kata/55d17ddd6d7868493e000074/python

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def append(listA, listB):
    currentNode = listA
    
    if currentNode is None:
        return listB
    elif listB is None:
        return listA
    
    while currentNode.next is not None:
        currentNode = currentNode.next
    
    currentNode.next = listB
    
    return listA
