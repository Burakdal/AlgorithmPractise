class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def deleteNode(head, position):
    index = 0
    current = head
    newHead = current
    if(head.next == None and position==0):
        return None
    if(position==0):
        return current.next
    while current != None:
        if (index == position - 1):
            current.next = current.next.next
        current = current.next
        index += 1
    return newHead


def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(16)

printLinkedList(deleteNode(head,0))
