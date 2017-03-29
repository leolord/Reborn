# coding=utf-8

u"""
插入排序
"""

import math


def find_place_to_insert(arr, start, end, key):
    u"""用二分法搜索插入排序的插入位置"""
    while True:
        if start == end:
            return end
        if start == end - 1:
            if arr[start] > key:
                return start
            else:
                return end

        mid = math.floor((start + end) / 2)

        if arr[mid] > key:
            end = mid
        else:
            start = mid


def insertion_sort_binary(arr):
    u"""用二分法优化插入排序"""
    arr_copy = arr.copy()
    arr_size = arr.size

    if arr_size < 2:
        return arr_copy

    for i in range(1, arr_size):
        key = arr_copy[i]
        place_to_insert = find_place_to_insert(arr_copy, 0, i, key)
        if i == place_to_insert:
            continue
        arr_copy[place_to_insert + 1:i + 1], arr_copy[place_to_insert] = arr_copy[place_to_insert:i], key

    return arr_copy


def insertion_sort(arr):
    u"""最原始的插入排序"""
    arr_copy = arr.copy()
    arr_size = arr.size

    if arr_size < 2:
        return arr_copy

    for i in range(1, arr_size):
        j = i - 1
        key = arr_copy[i]
        while j >= 0 and arr_copy[j] < key:
            arr_copy[j + 1] = arr_copy[j]
            j -= 1
        arr_copy[j + 1] = key
    return arr_copy
