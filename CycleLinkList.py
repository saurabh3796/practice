def has_cycle(head):
    if head is None:
        return 0
    temp = head
    temp1 = head
    while temp and temp1 and temp1.next:
        temp = temp.next
        temp1 = temp1.next.next
        if temp == temp1:
            return 1

    print(0)
    return 0
