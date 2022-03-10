# -*- codeing = utf-8 -*-
# @Time : 2022/3/10 23:25
# @Author : yolo
# @File : 2022.3.10.2的幂.py
# @Software: PyCharm
class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

