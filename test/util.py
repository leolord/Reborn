u"""一些测试用到的工具函数"""


def is_sorted(arr, inc=True):
    u"""判断一个数组是否已经排好序了"""
    idx = 1
    while idx < len(arr):
        nxt = arr[idx]
        pre = arr[idx - 1]
        if inc and pre > nxt:
            return False
        elif not inc and pre < nxt:
            return False
        idx += 1

    return True


def chunk(arr, size):
    for i in range(0, len(arr), size):
        yield arr[i: i + size]


def print_arr(arr):
    u"""完整的打印数组"""
    for i in chunk(arr, 16):
        print(i)
