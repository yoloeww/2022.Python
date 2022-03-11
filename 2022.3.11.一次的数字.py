# -*- codeing = utf-8 -*-
# @Time : 2022/3/11 23:11
# @Author : yolo
# @File : 2022.3.11.一次的数字.py
# @Software: PyCharm
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return reduce(lambda x, y: x ^ y, nums)

