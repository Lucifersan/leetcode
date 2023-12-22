#ew code but ig it works
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        rv = ListNode()
        currv = rv
        prevv = rv
        curr1 = l1
        curr2 = l2
        larger1 = True
        carryover = 0
        while curr1 != None and curr2 != None:
            temp = curr1.val + curr2.val + carryover
            carryover = temp//10
            currv.val = temp%10
            currv.next = ListNode()
            prevv=currv
            currv = currv.next
            curr1 = curr1.next
            curr2 = curr2.next
        curr = curr1 if curr1 != None else curr2
        while curr != None:
            temp = curr.val + carryover
            carryover = temp//10
            currv.val = temp%10
            prevv = currv
            currv.next = ListNode()
            currv = currv.next
            curr = curr.next
        curr = prevv.next
        curr.val = carryover
        if curr.val == 0:
            prevv.next=None
        return rv
        

        