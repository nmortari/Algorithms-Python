import SortingAlgorithms as SA
from Tools import Stopwatch,RandomArray



algorithm_list = [SA.InsertionSort,SA.QuickSort]
processing_time = []
tests_to_run = 10

for algorithm in algorithm_list:
    for test in range(tests_to_run):
        processing_time.append(Stopwatch.start(algorithm,RandomArray.LARGE, 23))
    print(algorithm.get_name() + "\n" + "Min: {:,} ns".format(min(processing_time)) + "\tMax: {:,} ns".format(max(processing_time)) + "\tAvg: {:,.0f} ns".format(sum(processing_time)/tests_to_run))
    processing_time.clear()


