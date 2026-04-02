"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        cp = head
        ohead = Node(cp.val)
        ocp = ohead

        while cp is not None:
            temp = cp
            cp = cp.next
            temp.next = ocp
            if cp is not None:
                ocp.next = Node(cp.val)
                ocp.random = cp
                ocp = ocp.next
        
        cp = head

        while cp is not None:
            temp = cp.next.random
            if cp.random is None:
                cp.next.random = None
            else:
                cp.next.random = cp.random.next
            cp = temp
        
        return ohead