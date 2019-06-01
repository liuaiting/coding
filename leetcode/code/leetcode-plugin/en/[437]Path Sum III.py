#You are given a binary tree in which each node contains an integer value. 
#
# Find the number of paths that sum to a given value. 
#
# The path does not need to start or end at the root or a leaf, but it must go downwards
#(traveling only from parent nodes to child nodes). 
#
# The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
#
# Example:
# 
#root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8
#
#      10
#     /  \
#    5   -3
#   / \    \
#  3   2   11
# / \   \
#3  -2   1
#
#Return 3. The paths that sum to 8 are:
#
#1.  5 -> 3
#2.  5 -> 2 -> 1
#3. -3 -> 11
# 
#

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: int
        """
        cache = {0: 1}
        self.res = 0
        self.preorder(root, 0, target, cache)
        return self.res

    def preorder(self, root, cur_sum, target, cache):
        if not root:
            return
        cur_sum += root.val
        old_sum = cur_sum - target
        self.res += cache.get(old_sum, 0)
        cache[cur_sum] = cache.get(cur_sum, 0) + 1
        self.preorder(root.left, cur_sum, target, cache)
        self.preorder(root.right, cur_sum, target, cache)
        cache[cur_sum] -= 1
