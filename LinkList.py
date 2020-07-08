
def printLinkedList(head):
    temp = head
    if head != None:
        while temp.next != None:
            print(temp.data)
            temp = temp.next 
        print(temp.data)
    else:
        print()

def insertNodeAtTail(head, data):
    if head == None:
        head = SinglyLinkedListNode(data)
    else:
        temp = head
        while temp.next != None:
            temp = temp.next
        temp1 = SinglyLinkedListNode(data)
        temp.next = temp1
    return head

def insertNodeAtHead(llist, data):
    temp = llist
    temp1 = SinglyLinkedListNode(data)
    if temp == None:
        llist = temp1
    else:
        temp1.next = llist
        llist = temp1
    return llist

def insertNodeAtPosition(head, data, position):
    temp = SinglyLinkedListNode(data)
    if head == None:
        head = temp
    else:
        temp1 = head
        i = 0
        while i < position-1:
            temp1 = temp1.next
            i = i + 1
        print(temp1.data)
        #print(temp)
        temp2 = temp1.next
        temp1.next = temp
        temp.next = temp2
    
    return head

def deleteNode(head, position):
    if head.next == None:
        head = None
        return head
    temp = head
    if position == 0:
        head = temp.next
        temp.next = None
        return head
    i = 0
    while i< position-1:
        temp = temp.next
        i+=1
    temp1 = temp.next
    temp.next = temp1.next
    temp1.next = None
    return head

def reverse(head):
    if head == None:
        return None
    current = head
    previous = None
    while current is not None:
        nxt = current.next
        current.next = previous
        previous = current
        current = nxt
    head = previous
    return head
