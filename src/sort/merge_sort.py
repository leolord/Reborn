# coding: utf-8

u"""
归并排序
"""

import math


def merge_arr(arr, start, mid, end):
    left_part = arr[start:mid]
    right_part = arr[mid:end]

    i = 0
    j = 0
    left_size = len(left_part)
    right_size = len(right_part)

    for k in range(start, end):
        if i >= left_size:
            arr[k] = right_part[j]
            j += 1
        elif j >= right_size:
            arr[k] = left_part[i]
            i += 1
        elif left_part[i] < right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1


def merge_sort(arr, start=0, end=-1):
    if end == -1:
        end = arr.size

    if start < end - 1:
        mid = int(math.floor((end + start) / 2))
        merge_sort(arr, start, mid)
        merge_sort(arr, mid, end)
        merge_arr(arr, start, mid, end)
