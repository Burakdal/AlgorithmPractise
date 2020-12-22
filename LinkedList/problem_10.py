class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def findMergeNode(head1, head2):
    nodeStore=dict()

    pointer1=head1
    pointer2=head2
    while pointer1 != None or pointer2 != None:
        if pointer1 in nodeStore:
            return pointer1

        if pointer2 in nodeStore:
            return pointer2

        nodeStore[pointer1.data]=pointer1.next
        nodeStore.add(pointer2.data)

        if pointer1:
            pointer1=pointer1.next

        if pointer2:
            pointer2=pointer1.next





def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(1)
head.next.next.next=SinglyLinkedListNode(1)
head.next.next.next.next=SinglyLinkedListNode(15)
head.next.next.next.next.next=SinglyLinkedListNode(19)
head.next.next.next.next.next.next=SinglyLinkedListNode(7)

head2 = SinglyLinkedListNode(5)
head2.next=SinglyLinkedListNode(3)
head2.next.next=SinglyLinkedListNode(15)
head2.next.next.next=SinglyLinkedListNode(19)
head2.next.next.next.next=SinglyLinkedListNode(7)

print(findMergeNode(head,head2).data)
