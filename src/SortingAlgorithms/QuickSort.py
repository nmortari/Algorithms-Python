import SortingAlgorithms.SAInterface as SAInterface


class QuickSort(SAInterface):


    @staticmethod
    def get_name():
        return "Quick Sort"

    @staticmethod
    def sort(array):
        # array = [1,8,3,9,4,5,7]
        left = []
        right = []
        if (len(array) > 1):
            for num in range(len(array)-1):
                if array[num] < array[-1]:
                    left.append(array[num])
                else:
                    right.append(array[num])
            # print(left)
            # print(right)
            # print(array)

            left = QuickSort.sort(left)
            left.extend(array[-1:])
            left.extend(QuickSort.sort(right))

            return left
        else:
            return array


# print(QuickSort.sort([1,8,3,9,4,5,7]))