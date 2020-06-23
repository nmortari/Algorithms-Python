from Tools.RandomArray import RandomArray
import time


class Stopwatch:

    @staticmethod
    def start(sorting_algorithm,array_specs,input_seed=time.time()):
        array = RandomArray.generate(array_specs.value,input_seed)

        start_time = time.perf_counter_ns()
        sorting_algorithm.sort(array)
        stop_time = time.perf_counter_ns()

        time_elapsed = (stop_time - start_time)

        print("Algorithm Type: " + sorting_algorithm.get_name() + "\t Array Size: " + array_specs.name + "\tTime: {:,} ns".format(time_elapsed))
        return time_elapsed
