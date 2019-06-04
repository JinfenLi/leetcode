class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def depth(root):
            if root==None:return 0
            L = depth(root.left)
            R = depth(root.right)
            self.ans = max(self.ans,L+R)
            return max(L,R)+1
        depth(root)
        return self.ans
if __name__ == '__main__':
    s=Solution()
    node1 = TreeNode(3)
    node2 = TreeNode(9)
    node3 = TreeNode(20)
    node4 = TreeNode(15)
    node5 = TreeNode(7)
    node1.left = node2
    node1.right = node3
    node3.left = node4
    node3.right = node5
    s.diameterOfBinaryTree(node1)
