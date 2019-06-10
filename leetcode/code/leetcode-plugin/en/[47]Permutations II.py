# coding=utf-8
# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example: 
#
# 
# Input: [1,1,2]
# Output:
# [
#  [1,1,2],
#  [1,2,1],
#  [2,1,1]
# ]
# 
#

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(tmp, size):
            if len(tmp) == size:
                res.append(tmp[:])
            else:
                for i in range(size):
                    if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                        continue
                    visited[i] = True
                    tmp.append(nums[i])
                    backtrack(tmp, size)
                    tmp.pop()
                    visited[i] = False

        res = []
        visited = [False] * len(nums)
        nums.sort()
        backtrack([], len(nums))
        return res
