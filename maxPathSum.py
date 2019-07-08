# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def max_gain(node):
            nonlocal max_sum
            if not node:
                return 0

            # max sum on the left and right sub-trees of node
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            # the price to start a new path where `node` is a highest node
            price_newpath = node.val + left_gain + right_gain

            # update max_sum if it's better to start a new path
            max_sum = max(max_sum, price_newpath)

            # for recursion :
            # return the max gain if continue the same path
            return node.val + max(left_gain, right_gain)

        max_sum = float('-inf')
        max_gain(root)
        print(max_sum)
        return max_sum

if __name__ == '__main__':
    s=Solution()
    node1=TreeNode(-10)
    node2=TreeNode(-9)
    node3=TreeNode(-20)
    # node4=TreeNode(15)
    # node5=TreeNode(7)
    node1.left=node2
    node1.right=node3
    # node3.left=node4
    # node3.right=node5
    s.maxPathSum(node1)
