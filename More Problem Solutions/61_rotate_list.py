'''
Given the head of a linked list, rotate the list to the right by k places.

 

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109

'''

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        total_length = 1
        dummy = head

        while dummy.next:
            dummy = dummy.next
            total_length += 1

        slow, fast = k % total_length, head
        if slow == 0:
            return head

        counter = 0
        while counter < (total_length - slow - 1):
            fast = fast.next
            counter += 1

        result_head = fast.next
        fast.next = None
        dummy.next = head
        return result_head

if __name__ == '__main__':
    head_list = [1,2,3,4,5]
    k = 2


    dummy = ListNode()
    current = dummy

    for val in head_list:
        current.next = ListNode(val)
        current = current.next

    head = dummy.next

    result_head = Solution().rotateRight(head=head, k=k)

    while result_head:
        print(result_head.val, end=" -> ")
        result_head = result_head.next
