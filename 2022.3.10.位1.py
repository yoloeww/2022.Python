# -*- codeing = utf-8 -*-
# @Time : 2022/3/10 23:26
# @Author : yolo
# @File : 2022.3.10.位1.py
# @Software: PyCharm
class Solution:
    def hammingWeight(self, n: int) -> int:
        ret = sum(1 for i in range(32) if n & (1 << i))
        return ret

