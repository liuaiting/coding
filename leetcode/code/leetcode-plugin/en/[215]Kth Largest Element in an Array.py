# coding=utf-8
# Find the kth largest element in an unsorted array. Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Example 1: 
#
# 
# Input: [3,2,1,5,6,4] and k = 2
# Output: 5
# 
#
# Example 2: 
#
# 
# Input: [3,2,3,1,2,4,5,5,6] and k = 4
# Output: 4
#
# Note: 
# You may assume k is always valid, 1 ≤ k ≤ array's length.
#
import heapq


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # 最小堆
        heap = nums[:k]
        heapq.heapify(heap)
        for i in range(k, len(nums)):
            if nums[i] > heap[0]:
                heapq.heappushpop(heap, nums[i])
        return heap[0]


nums = [3, 2, 1, 5, 6, 4]
s = Solution()
print(s.findKthLargest(nums, 2))


#
# import random
#
#
# class Solution2(object):
#     def findKthLargest(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: int
#         """
#         # 快排 partition
#         left, right = 0, len(nums) - 1
#         while left <= right:
#             pivot_idx = random.randint(left, right)
#             new_pivot_idx = self.PartitionAroundPivot(left, right, pivot_idx, nums)
#             if new_pivot_idx == k - 1:
#                 return nums[new_pivot_idx]
#             elif new_pivot_idx > k - 1:
#                 right = new_pivot_idx - 1
#             else:
#                 left = new_pivot_idx + 1
#
#     def PartitionAroundPivot(self, left, right, pivot_idx, nums):
#         pivot_value = nums[pivot_idx]
#         new_pivot_idx = left
#         nums[pivot_idx], nums[right] = nums[right], nums[pivot_idx]
#         for i in range(left, right):
#             if nums[i] > pivot_value:
#                 nums[i], nums[new_pivot_idx] = nums[new_pivot_idx], nums[i]
#                 new_pivot_idx += 1
#         nums[right], nums[new_pivot_idx] = nums[new_pivot_idx], nums[right]
#         return new_pivot_idx
#
#
# nums = [3, 2, 1, 5, 6, 4]
# s = Solution2()
# res = s.findKthLargest(nums, 2)
# print(res)
