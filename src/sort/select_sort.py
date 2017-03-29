u"""选择排序"""


def select_sort(arr, start, end):
    u"""
    选择排序，每次在剩余数组中选择最小的与当前元素交换
    :param arr: 要排序的数组
    :param start: 要排序的起始坐标（包含）
    :param end: 要排序的终止坐标（不包含）
    :return: 排序好的数组
    """
    while start < end - 1:
        minimal_index = start

        for i in range(start + 1, end):
            if arr[i] < arr[minimal_index]:
                minimal_index = i

        arr[start], arr[minimal_index] = arr[minimal_index], arr[start]
        start += 1

    return arr
