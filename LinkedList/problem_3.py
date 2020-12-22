class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def reversePrint(head):
    newArray = list()
    current = head
    while current != None:
        newArray.append(current.data)
        current = current.next
    for i in reversed(newArray):
        print(i)


def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next

head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(1)
head.next.next.next=SinglyLinkedListNode(7)

reversePrint(head)
