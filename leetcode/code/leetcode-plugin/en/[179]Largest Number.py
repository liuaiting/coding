# Given a list of non negative integers, arrange them such that they form the largest number.
#
# Example 1: 
#
# 
# Input: [10,2]
# Output: "210"
#
# Example 2: 
#
# 
# Input: [3,30,34,5,9]
# Output: "9534330"
# 
#
# Note: The result may be very large, so you need to return a string instead of an integer. 
#

class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        array = list(map(str, nums))
        array.sort(cmp=lambda x, y: cmp(x + y, y + x), reverse=True)
        return "0" if array[0] == "0" else "".join(array)


test = Solution()
print(test.largestNumber([3, 30, 34, 5, 9]))
