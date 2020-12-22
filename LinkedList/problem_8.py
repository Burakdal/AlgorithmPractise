class SinglyLinkedListNode:

    def __init__(self,data):
        self.data=data
        self.next=None

#problem
def removeDuplicates(head):
    counterDict=dict()

    current=head

    while current != None:
        if current.data not in counterDict.keys():
            counterDict[current.data]=1
        else:
            counterDict[current.data] += 1
        if current.next != None and current.next.data in counterDict.keys():
            if current.next.next != None:
                current.next =current.next.next
            else:
                current.next = None
        else:
            current = current.next
    return head




def printLinkedList(node):
    current=node
    while current != None:
        print(current.data)
        current=current.next


head = SinglyLinkedListNode(16)
head.next=SinglyLinkedListNode(13)
head.next.next=SinglyLinkedListNode(1)
head.next.next.next=SinglyLinkedListNode(1)
head.next.next.next.next=SinglyLinkedListNode(1)
head.next.next.next.next.next=SinglyLinkedListNode(7)

printLinkedList(removeDuplicates(head))
