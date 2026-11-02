# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        if head == None or head.next == None:
            return head

        l = 0
        last = head
        while last.next != None:
            last = last.next
            l +=1
        l +=1

        k %=l
        if k ==0:
            return head

        current = head
        for i in range(l - k - 1):
            current = current.next

        last.next = head
        head = current.next
        current.next = None

        return head    


        