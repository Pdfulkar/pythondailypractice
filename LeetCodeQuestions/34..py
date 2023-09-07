# 34.
# Find
# First and Last
# Position
# of
# Element in Sorted
# Array
# Medium
# 18.4
# K
# 446
# Companies
# Given
# an
# array
# of
# integers
# nums
# sorted in non - decreasing
# order, find
# the
# starting and ending
# position
# of
# a
# given
# target
# value.
#
# If
# target is not found in the
# array,
# return [-1, -1].
#
# You
# must
# write
# an
# algorithm
# with O(log n) runtime complexity.
#
# Example
# 1:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 8
# Output: [3, 4]
# Example
# 2:
#
# Input: nums = [5, 7, 7, 8, 8, 10], target = 6
# Output: [-1, -1]
# Example
# 3:
#
# Input: nums = [], target = 0
# Output: [-1, -1]

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # lo, hi = 0, len(nums)-1
        # Output_list = []
        # while lo < hi:
        #     mid = (lo + hi)//2
        #     mid_num = nums[mid]
        #     print(lo , mid, hi , mid_num)
        #     if mid_num == target:
        #         Output_list.append(mid)
        #     if mid_num < target:
        #         hi = mid - 1
        #     elif mid_num > target:
        #         lo = mid + 1
        # Output_list.append([-1,-1])
        # return Output_list



        # tryed the solution but the time is exceeding the solution
        class Solution(object):
            def searchRange(self, nums, target):
                """
                :type nums: List[int]
                :type target: int
                :rtype: List[int]
                """
                lo, hi = 0, len(nums) - 1
                Output_list = []
                while lo < hi:
                    mid = (lo + hi) // 2
                    mid_num = nums[mid]
                    if mid_num == target:
                        Output_list.append(mid)
                        if (nums[mid + 1] == target):
                            Output_list.append(mid + 1)
                            break
                        elif (nums[mid - 1] == target):
                            Output_list.append(mid - 1)
                            break
                    elif mid_num > target:
                        hi = mid - 1
                        if hi == 0:
                            break
                    elif mid_num < target:
                        lo = mid + 1
                        if lo == mid:
                            break
                Output_list.sort()
                if (len(Output_list) == 1):
                    Output_list.append(Output_list[0])
                if (len(nums) == 1 and nums[0] == target):
                    Output_list.append(0)
                    Output_list.append(0)
                if len(Output_list) == 0:
                    Output_list.append(-1)
                    Output_list.append(-1)
                return Output_list
