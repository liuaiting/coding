# coding=utf-8
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# 
#
# 
# For example, given n = 3, a solution set is:
# 
# 
# [
#  "((()))",
#  "(()())",
#  "(())()",
#  "()(())",
#  "()()()"
# ]
#

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        def backtrack(s, left, right):
            if len(s) == 2 * n:
                res.append(s)
                return
            if left < n:
                backtrack(s + "(", left + 1, right)
            if right < left:
                backtrack(s + ")", left, right + 1)

        res = []
        backtrack("", 0, 0)
        return res
