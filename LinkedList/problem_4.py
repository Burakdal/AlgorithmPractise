class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def reverse(head):
    newNodeHead=SinglyLinkedListNode(None)
    current=head
    while current != None:
        newNode=SinglyLinkedListNode(current.data)
        newNode.next=newNodeHead.next
        newNodeHead.next=newNode
        current=current.next
    return newNodeHead.next



def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(1)
head.next.next.next=SinglyLinkedListNode(7)

printLinkedList(reverse(head))
