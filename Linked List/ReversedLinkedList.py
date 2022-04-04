class Solution:
    def reverseList(self, head):
        prev, temp = None, None
        while head:
            temp = head.next 
            head.next = prev
            prev = head
            head = temp 
        
        return prev
        