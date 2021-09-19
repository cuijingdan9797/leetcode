'''142. 环形链表 II'''



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # 弗洛伊德算法：快慢指针相遇后将fast放回链表开始每次走一步，slow继续走，他们会在环口相遇
        if not head or not head.next: return None
        slow = head
        fast = head
        hasCycle = False
        while slow and fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                hasCycle = True
                break
        if hasCycle:
            fast = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return slow
        else:
            return None