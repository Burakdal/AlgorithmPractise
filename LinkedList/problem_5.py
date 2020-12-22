class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def compare_lists(llist1, llist2):
    current1=llist1
    current2=llist2

    if current1 == None and current2 == None:
        return 1

    while current1!=None and current2 != None:
        if current1.data != current2.data:
            return 0
        current1=current1.next
        current2=current2.next
    if current1!=None or current2 !=None:
        return 0
    return 1


def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(1)
head.next.next.next=SinglyLinkedListNode(7)

head2 = SinglyLinkedListNode(16)
head2.next=SinglyLinkedListNode(13)
head2.next.next=SinglyLinkedListNode(1)
head2.next.next.next=SinglyLinkedListNode(8)

print(compare_lists(head,head2))
