# coding=utf-8
# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets. 
#
# Example: 
#
# 
# Input: nums = [1,2,3]
# Output:
# [
#  [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]
#

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, start, end):
            res.append(tmp[:])
            for i in range(start, end):
                tmp.append(nums[i])
                backtrack(tmp, i + 1, end)
                tmp.pop()

        res = []
        backtrack([], 0, len(nums))
        return res
