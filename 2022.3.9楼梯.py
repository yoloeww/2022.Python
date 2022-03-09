# -*- codeing = utf-8 -*-
# @Time : 2022/3/9 23:51
# @Author : yolo
# @File : 2022.3.9楼梯.py
# @Software: PyCharm


class Solution:
    def climbStairs(self, n: int) -> int:
        #斐波那契数列前两项；
        a, b = 1, 1
        #前三项Sn就是nn，所以从第4项开始计算，预设初始答案S3；
        ans = 3
        # 小于3返回n；
        if n <= 3:
            return n
        #从第4项开始计算，斐波那契数列求和；
        for i in range(4, n + 1):
            ans += a + b
            a, b = b, a + b
        return ans

