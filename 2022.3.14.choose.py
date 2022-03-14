# -*- codeing = utf-8 -*-
# @Time : 2022/3/14 23:36
# @Author : yolo
# @File : 2022.3.14.choose.py
# @Software: PyCharm

def find(arr):
    smallest=arr[0]
    smallest_index=0
    for i in range (1,len(arr)):
        if arr[i]<smallest:
            smallest=arr[i]
            smallest_index=i
    return smallest_index

def select(arr):
    new=[]
    for i in range (len(arr)):
        smallest=find(arr)
        new.append(arr.pop(smallest))
    return new

b=[1,3,4,3]
print(select[b])