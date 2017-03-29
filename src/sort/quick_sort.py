u"""快速排序"""


def quick_sort(arr, start, end):
    call_stack = [(start, end)]

    while len(call_stack) > 0:
        start, end = call_stack.pop()

        if start > end - 2:
            continue

        if start == end - 2:
            if arr[start] > arr[end - 1]:
                arr[start], arr[end - 1] = arr[end - 1], arr[start]
            continue

        pivot = arr[start]
        store_index = start + 1

        for ite in range(store_index, end):
            if arr[ite] < pivot:
                arr[store_index], arr[ite] = arr[ite], arr[store_index]
                store_index += 1

        arr[store_index - 1], arr[start] = arr[start], arr[store_index - 1]

        call_stack.append((start, store_index - 1))
        call_stack.append((store_index, end))

    return arr
