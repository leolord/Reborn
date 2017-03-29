u"""基数排序"""
import numpy as np
import math


def radix_sort(arr, radix=10):
    u"""
    基数排序
    :param arr: 需要排序的数组
    :return: 排序好的数组
    """
    if isinstance(arr, np.ndarray):
        arr = arr.tolist()

    K = int(math.ceil(math.log(max(arr), radix)))
    buckets = [[] for i in range(0, radix)]

    for i in range(0, K + 1):
        for val in arr:
            bucket_index = int(val % (radix ** i) / (radix ** (i - 1)))
            buckets[bucket_index].append(val)

        del arr[:]

        for bucket in buckets:
            arr.extend(bucket)
            del bucket[:]

    return arr
