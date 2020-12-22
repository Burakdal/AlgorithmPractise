class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def has_cycle(head):
    slow_p = head
    fast_p = head
    while slow_p != None and fast_p != None and fast_p.next != None:
        slow_p = slow_p.next
        fast_p = fast_p.next.next

        if slow_p == fast_p:
            return 1
    return 0





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

print(has_cycle(head))
