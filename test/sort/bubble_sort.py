import time
import unittest

import numpy as np

from src.sort.bubble_sort import bubble_sort, bubble_sort_2
from test.util import is_sorted


class TestBubbleSort(unittest.TestCase):
    u"""测试冒泡排序"""

    def test_bubble_sort(self):
        arr = np.random.random_integers(-100, 100, 3000)
        begin_time = time.time()
        bubble_sort(arr, 0, len(arr))
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '冒泡排序的结果非升序')
        print('%f ms used' % (end_time - begin_time))

    def test_bubble_sort_speed(self):
        arr = np.random.random_integers(-100, 100, 5000)
        arr_copy = arr.copy()

        begin_time = time.time()
        bubble_sort(arr, 0, len(arr))
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '基础的冒泡排序算法非升序')
        print('基础版本的冒牌排序耗时 %f 秒' % (end_time - begin_time))

        begin_time = time.time()
        bubble_sort_2(arr_copy, 0, len(arr))
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '优化的冒泡排序算法非升序')
        print('优化版本的冒牌排序耗时 %f 秒' % (end_time - begin_time))