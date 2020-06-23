import SortingAlgorithms.SAInterface as SAInterface


class InsertionSort(SAInterface):

    @staticmethod
    def get_name():
        return "Insertion Sort"

    @staticmethod
    def sort(array):
        for index in range(len(array) - 1):
            if (array[index + 1] < array[index]):
                for sort in range(len(array) - 1):
                    if (array[index + 1] < array[sort]):
                        array.insert(sort, array[index + 1])
                        array.pop(index + 2)
                        break
        return array