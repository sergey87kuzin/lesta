import unittest


def partition(array, pivot):
    left = []
    center = []
    right = []
    for element in array:
        if element < pivot:
            left.append(element)
        elif element > pivot:
            right.append(element)
        else:
            center.append(element)
    return left, center, right


def quicksort(array):
    array_len = len(array)
    if array_len < 2:
        return array
    else:
        pivot = array[array_len // 2]
        left, center, right = partition(array, pivot)
        return quicksort(left) + center + quicksort(right)


class MySortTest(unittest.TestCase):

    def test_sorting(self):
        array = [6, 3, 9, 10, 0, -8, 135, 54]
        sorted_array = quicksort(array)
        self.assertListEqual(sorted_array, sorted(array))


if __name__ == '__main__':
    unittest.main()
