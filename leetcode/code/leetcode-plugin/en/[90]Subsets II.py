# coding=utf-8
# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets. 
#
# Example: 
#
# 
# Input: [1,2,2]
# Output:
# [
#  [2],
#  [1],
#  [1,2,2],
#  [2,2],
#  [1,2],
#  []
# ]
# 
#

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        def backtrack(tmp, start, end):
            res.append(tmp[:])
            for i in range(start, end):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                tmp.append(nums[i])
                backtrack(tmp, i + 1, end)
                tmp.pop()
        res = []
        nums.sort()
        backtrack([], 0, len(nums))
        return res


test = Solution()
test.subsetsWithDup([1, 2, 2])
