# coding=utf-8
# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example: 
#
# 
# Input: n = 4, k = 2
# Output:
# [
#  [2,4],
#  [3,4],
#  [2,3],
#  [1,2],
#  [1,3],
#  [1,4],
# ]
# 
#

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        def backtrack(tmp, start, k):
            if k == 0:
                res.append(tmp[:])
                return
            for i in range(start, n + 1):
                tmp.append(i)
                backtrack(tmp, i + 1, k - 1)
                tmp.pop()

        res = []
        backtrack([], 1, k)
        return res


test = Solution()
print(test.combine(4, 2))
