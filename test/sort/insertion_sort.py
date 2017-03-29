import time
import unittest

import numpy as np

from src.sort.insertion_sort import\
    insertion_sort,\
    find_place_to_insert,\
    insertion_sort_binary
from test.util import is_sorted


class TestInsertionSort(unittest.TestCase):
    u"""插入排序的测试用例"""

    def test_binary_search(self):
        u"""测试二分搜索方法"""
        arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.assertEqual(find_place_to_insert(arr, 0, len(arr), 1), 1, '第一个元素')
        self.assertEqual(find_place_to_insert(arr, 0, len(arr), 0), 0, '第一个元素之前')
        self.assertEqual(find_place_to_insert(arr, 0, len(arr), 30), 9, '最后一个元素之后')
        self.assertEqual(find_place_to_insert(arr, 0, len(arr), 4), 4, '第四个元素')

    def test_swap(self):
        u"""测试列表的swap方法"""
        arr = [1, 2, 3]
        arr[0:2], arr[2] = arr[1:3], arr[0]
        self.assertEqual(arr, [2, 3, 1])

    def test_insertion_sort_binary(self):
        """测试优化过的插入排序"""
        test_size = 1024 * 8
        test_arr = np.random.randint(-100, 100, test_size)

        print('Begin Test Binary Insertion Sort')

        begin_time = time.time()
        result_arr = insertion_sort_binary(test_arr)
        end_time = time.time()

        self.assertTrue(is_sorted(result_arr))
        print('%f ms used' % (end_time - begin_time))
        print('-' * 80)
        print()

    def test_insertion_sort(self):
        """测试原始的插入排序"""
        test_size = 1024 * 8
        test_arr = np.random.randint(-100, 100, test_size)

        print('Begin Test Insertion Sort')

        begin_time = time.time()
        result_arr = insertion_sort(test_arr)
        end_time = time.time()

        self.assertTrue(is_sorted(result_arr))
        print('%f ms used' % (end_time - begin_time))
        print('-' * 80)
        print()


if __name__ == '__main__':
    unittest.main()
