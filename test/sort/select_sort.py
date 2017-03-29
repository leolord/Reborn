import time
import unittest

import numpy as np

from src.sort.select_sort import select_sort
from test.util import is_sorted


class TestSelectSort(unittest.TestCase):
    u"""测试选择排序"""

    def test_bubble_sort(self):
        arr = np.random.random_integers(-100, 100, 3000)
        begin_time = time.time()
        select_sort(arr, 0, len(arr))
        end_time = time.time()

        self.assertTrue(is_sorted(arr), '选择排序的结果非升序')
        print('排序用时: %f 秒' % (end_time - begin_time))
