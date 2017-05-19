# https://www.hackerrank.com/challenges/detect-whether-a-linked-list-contains-a-cycle

"""
Detect a cycle in a linked list. Note that the head pointer may be 'None' if the list is empty.

A Node is defined as: 
 
    class Node(object):
        def __init__(self, data = None, next_node = None):
            self.data = data
            self.next = next_node
"""

# hare and tortoise method for loop detection.

def has_cycle(head):
    slow = head
    fast = head.next
    
    while slow.next and fast.next.next:
        if slow == fast:
            return 1
        slow = slow.next
        fast = fast.next.next
    return 0
