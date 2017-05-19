# https://www.hackerrank.com/challenges/merge-two-sorted-linked-lists

"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as
 
 class Node(object):
 
   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""
def MergeLists(headA, headB):
    if not headA:
        return headB
    elif not headB:
        return headA
    elif headA.data < headB.data:
        restA = headA.next
        headA.next = MergeLists(restA, headB)
        return headA
    else:
        restB = headB.next
        headB.next = MergeLists(restB, headA)
        return headB
