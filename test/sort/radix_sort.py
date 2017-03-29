import time
import unittest

import numpy as np

from src.sort.radix_sort import radix_sort
from test.util import is_sorted


class TestRadixSort(unittest.TestCase):
    u"""测试基数排序"""

    def test_radix_sort(self):
        arr = np.random.random_integers(0, 99, 300000)
        begin_time = time.time()
        arr = radix_sort(arr)
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '基数排序的结果非升序')
        print('排序用时: %f 秒' % (end_time - begin_time))
