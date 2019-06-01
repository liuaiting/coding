# coding=utf-8
#Given a matrix A, return the transpose of A.
#
# The transpose of a matrix is the matrix flipped over it's main diagonal, switching the row and column indices of the matrix. 
#
# 
#
# 
# Example 1: 
#
# 
#Input: [[1,2,3],[4,5,6],[7,8,9]]
#Output: [[1,4,7],[2,5,8],[3,6,9]]
# 
#
# 
# Example 2: 
#
# 
#Input: [[1,2,3],[4,5,6]]
#Output: [[1,4],[2,5],[3,6]]
# 
#
# 
#
# Note: 
#
# 
# 1 <= A.length <= 1000 
# 1 <= A[0].length <= 1000 
# 
# 
# 
#

class Solution(object):
    def transpose(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        # 注意深拷贝浅拷贝的问题
        # 列表的复制问题，当外层列表里面仍存在列表时，若对外层列表进行复制，
        # 此时内层列表是原列表的引用，对一个进行修改，另一个也会同时发生变化
        R, C = len(A), len(A[0])
        B = [[None for i in range(R)] for j in range(C)]
        for r, row in enumerate(A):
            for c, val in enumerate(row):
                B[c][r] = val
        return B


test = Solution()
print(test.transpose([[1,2,3],[4,5,6]]))