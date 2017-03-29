u'''
冒泡排序
'''


def bubble_sort(arr, start, end):
    u"""
    冒泡排序
    :param arr: 用于排序的数组
    :param start: 排序的起始坐标（包含）
    :param end: 排序的种植坐标(不包含)
    :return: 排序好的数组
    """
    while True:
        swapped = False
        for i in range(start, end - 1):
            j = i + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
                swapped = True
        if not swapped:
            break
    return arr

def bubble_sort_2(arr, start, end):
    u"""
    优化过的冒泡排序，理论上会快一倍
    :param arr: 用于排序的数组
    :param start: 排序的起始坐标（包含）
    :param end: 排序的终止坐标（不包含）
    :return: 排序好的数组
    """
    end_point = end
    while end_point > start:
        for i in range(start, end_point - 1):
            j = i + 1
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]
        end_point -= 1
    return arr
