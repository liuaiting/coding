# coding=utf-8
# Given a string s, partition s such that every substring of the partition is a palindrome.
#
# Return all possible palindrome partitioning of s. 
#
# Example: 
#
# 
# Input: "aab"
# Output:
# [
#  ["aa","b"],
#  ["a","a","b"]
# ]
# 
#

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def backtrack(tmp, start, end):
            if start == end:
                res.append(tmp[:])
            for i in range(start, end):
                cur = s[start: i + 1]
                if cur == cur[::-1]:
                    tmp.append(cur)
                    backtrack(tmp, i + 1, end)
                    tmp.pop()

        res = []
        backtrack([], 0, len(s))
        return res
