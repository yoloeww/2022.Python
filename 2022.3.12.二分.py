# -*- codeing = utf-8 -*-
# @Time : 2022/3/12 17:45
# @Author : yolo
# @File : 2022.3.12.二分.py
# @Software: PyCharm
my_list=[1,3,5,7,9]
def binary_search(list,item):
 low=0
 high=len(list)-1
 while low <= high:
    mid=int((low+high)/2)
    guess=list[mid]
    if guess==item:
        return mid
    if guess >item:
        high=mid-1
    else:
        low=mid+1
 return None
print(binary_search(my_list,5))