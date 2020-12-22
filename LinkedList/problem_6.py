class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def mergeLists(head1, head2):
    newNodeHead=SinglyLinkedListNode(None)

    current1=head1
    current2=head2

    currentNode=newNodeHead

    while  current1 != None or current2!=None:
        if current1 != None and current2!=None and  current1.data < current2.data:
            currentNode.next=current1
            current1=current1.next
        elif current1 != None and current2!=None and  current1.data >= current2.data:
            currentNode.next = current2
            current2 = current2.next
        elif current1!=None:
            currentNode.next=current1
            current1=current1.next
        elif current2!=None:
            currentNode.next=current2
            current2 = current2.next

        currentNode=currentNode.next

    return  newNodeHead.next


def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(1)
head.next=SinglyLinkedListNode(7)
head.next.next=SinglyLinkedListNode(13)
head.next.next.next=SinglyLinkedListNode(16)

head2 = SinglyLinkedListNode(2)
head2.next=SinglyLinkedListNode(4)
head2.next.next=SinglyLinkedListNode(6)
head2.next.next.next=SinglyLinkedListNode(11)

printLinkedList(mergeLists(head,head2))
