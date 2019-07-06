# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    # def lowestCommonAncestor(self, root, p, q):
    #     """
    #     :type root: TreeNode
    #     :type p: TreeNode
    #     :type q: TreeNode
    #     :rtype: TreeNode
    #     """
    #     # list1 = self.dfs(root, [], p)
    #     # list2 = self.dfs(root, [], q)
    #     # if len(list2) < len(list1):
    #     #     list1, list2 = list2, list1
    #     #
    #     # for i in range(len(list1)):
    #     #     if list1[i] != list2[i]:
    #     #         return list1[i]
    #     #     if i == len(list1) - 1:
    #     #         return list1[-1]
    #     if self.findNode(root.left, p):
    #         if self.findNode(root.right, q):
    #             return root
    #         else:
    #             return self.lowestCommonAncestor(root.left, p, q)
    #     else:
    #         if self.findNode(root.left, q):
    #             return root
    #         else:
    #             return self.lowestCommonAncestor(root.right, p, q)
    #
    # def findNode(self,root, node):
    #     if not root or not node:
    #         return False
    #     if root == node:
    #         return True
    #     found = self.findNode(root.left, node)
    #     if not found:
    #         found = self.findNode(root.right, node)
    #     return found

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        def recurse_tree(current_node):

            # If reached the end of a branch, return False.
            if not current_node:
                return False

            # Left Recursion
            left = recurse_tree(current_node.left)

            # Right Recursion
            right = recurse_tree(current_node.right)

            # If the current node is one of p or q
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            # Return True if either of the three bool values is True.
            return mid or left or right

        # Traverse the tree
        recurse_tree(root)
        return self.ans

    def lowestCommonAncestor2(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """

        # Stack for tree traversal
        stack = [root]

        # Dictionary for parent pointers
        parent = {root: None}

        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:

            node = stack.pop()

            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()

        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]

        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q

if __name__ == '__main__':
    s=Solution()
    node1=TreeNode(3)
    node2=TreeNode(5)
    node3=TreeNode(6)
    node4=TreeNode(2)
    node5=TreeNode(7)
    node6=TreeNode(4)
    node7=TreeNode(1)
    node8=TreeNode(0)
    node9=TreeNode(8)
    node1.left=node2
    node2.left=node3
    node2.right=node4
    node4.left=node5
    node4.right=node6
    node1.right=node7
    node7.left=node8
    node7.right=node9
    # s.dfs(node1,[],node9)
    s.lowestCommonAncestor(node1,node4,node8)
