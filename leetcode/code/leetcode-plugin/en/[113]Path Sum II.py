# coding=utf-8
#Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
#
# Note: A leaf is a node with no children. 
#
# Example: 
#
# Given the below binary tree and sum = 22, 
#
# 
#      5
#     / \
#    4   8
#   /   / \
#  11  13  4
# /  \    / \
#7    2  5   1
# 
#
# Return: 
#
# 
#[
#   [5,4,11,2],
#   [5,8,4,5]
#]
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
        :rtype: List[List[int]]
        """
        if not root:
            return None
        res = []
        self.preorder(root, target, [], res)
        return res

    def preorder(self, root, target, path, res):
        if not root:
            return
        path.append(root.val)
        if not root.left and not root.right and target == root.val:
            res.append(list(path))
        self.preorder(root.left, target-root.val, path, res)
        self.preorder(root.right, target-root.val, path, res)
        path.pop()
