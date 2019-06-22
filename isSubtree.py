# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(s, t):
            if s == None and t == None:
                return True
            if s == None or t == None:
                return False

            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)

        def traverse(s, t):
            return s != None and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))

        return traverse(s, t)

