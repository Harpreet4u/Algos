# https://www.hackerrank.com/challenges/get-the-value-of-the-node-at-a-specific-position-from-the-tail

#Body
"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""

# Two pointer technique without using length of linked list.

def GetNode(head, position):    
    first_position = position
    first = head
    while first_position:
        first = first.next
        first_position -= 1
    
    second = head
    while first.next:
        second = second.next
        first = first.next
    return second.data
