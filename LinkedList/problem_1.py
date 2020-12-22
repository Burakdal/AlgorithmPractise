class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

def insertNodeAtPosition(head, data, position):
    index=0
    current=head
    newHead = current
    while current != None:
        if(index == position-1):
            newNode=SinglyLinkedListNode(data)
            newNode.next=current.next
            current.next = newNode
        current=current.next
        index +=1
    return newHead


def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next



head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(7)

printLinkedList(insertNodeAtPosition(head,1,2))
