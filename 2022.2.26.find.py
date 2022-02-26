# -*- codeing = utf-8 -*-
# @Time : 2022/2/26 11:03
# @Author : 奇奇
# @File : 2022.2.26.find.py
# @Software: PyCharm

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left,right  =0, len(nums)
        while left < right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid
            else:
                return mid
        return -1