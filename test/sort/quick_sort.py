import time
import unittest

import numpy as np

from src.sort.quick_sort import quick_sort
from test.util import is_sorted


class TestQuickSort(unittest.TestCase):
    u"""测试快速排序"""

    def test_quick_sort(self):
        arr = np.random.random_integers(-100, 100, 300000)
        begin_time = time.time()
        quick_sort(arr, 0, len(arr))
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '快速排序的结果非升序')
        print('排序用时: %f 秒' % (end_time - begin_time))
