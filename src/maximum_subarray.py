# coding=utf-8

u"""
计算最大子数组.

用算法导论中最朴素的分治法
"""

import math


def find_max_crossing_subarray(arr, low, mid, high):
    u"""计算跨越中间点的最大子数组."""
    left_sum = -math.inf
    total_sum = 0.0
    max_left = mid
    for i in range(mid, low, -1):
        total_sum += arr[i]
        if total_sum > left_sum:
            left_sum = total_sum
            max_left = i

    right_sum = -math.inf
    total_sum = 0.0
    max_right = mid + 1
    for j in range(mid + 1, high):
        total_sum += arr[j]
        if total_sum > right_sum:
            right_sum = total_sum
            max_right = j
    return max_left, max_right, left_sum + right_sum


def find_max_subarray(arr, low, high):
    u"""递归计算最大子数组."""
    if high == low:
        result = (low, high, arr[low])
    elif high == low + 1:
        if arr[low] > 0 and arr[high] > 0:
            result = (low, high, arr[low] + arr[high])
        elif arr[low] > arr[high]:
            result = (low, low, arr[low])
        else:
            result = (high, high, arr[high])
    else:
        mid = (low + high) // 2

        (left_low, left_high, left_sum) = find_max_subarray(arr, low, mid)

        (right_low, right_high, right_sum) = find_max_subarray(arr, mid + 1, high)

        (cross_low, cross_high, cross_sum) = find_max_crossing_subarray(arr, low, mid, high)

        if left_sum >= right_sum and left_sum >= cross_sum:
            result = (left_low, left_high, left_sum)
        elif right_sum >= left_sum and right_sum >= cross_sum:
            result = (right_low, right_high, right_sum)
        else:
            result = (cross_low, cross_high, cross_sum)

    return result


def find_mas_subarray_linear(arr):
    u"""用朴素的从左向右扫描确定最大子数组
    基本的想法是，遍历arr，同时记录左边最小的数值，两者差值为临时最大子数组的和
    """
    tmp_sum = 0
    original_stuck_trend = []
    for i in arr:
        tmp_sum += i
        original_stuck_trend.append(tmp_sum)

    minimal_price = math.inf
    minimal_index = -math.inf
    max_sum = 0
    start_index = -1
    end_index = -1

    for idx in range(0, len(original_stuck_trend) - 1):
        i = original_stuck_trend[idx]
        if i < minimal_price:
            minimal_price = i
            minimal_index = idx
        else:
            tmp_sum = i - minimal_price
            if tmp_sum > max_sum:
                max_sum = tmp_sum
                start_index = minimal_index
                end_index = idx

    return start_index, end_index, max_sum



