import SortingAlgorithms as SA
from Tools import Stopwatch,RandomArray



algorithm_list = [SA.InsertionSort]
processing_time = []
tests_to_run = 10

for algorithm in algorithm_list:
    for test in range(tests_to_run):
        processing_time.append(Stopwatch.start(algorithm,RandomArray.LARGE, 23))
    print("Min: {:,} ns".format(min(processing_time)) + "\tMax: {:,} ns".format(max(processing_time)) + "\tAvg: {:,}".format(sum(processing_time)/tests_to_run))

