# Definition for singly-linked list.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast, slow = head, dummy

        while n > 0:
            fast = fast.next
            n-=1
            
        while fast:
            fast = fast.next
            slow = slow.next
        

        slow.next = slow.next.next

        return dummy.next