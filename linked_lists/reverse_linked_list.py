# Recursive algo for reversing linked list.


def reverse_list(head):

    if head.next == None:
        return head

    newHead = reverse_list(head.next)
    head.next.next = head
    head.next = None
    return newHead

