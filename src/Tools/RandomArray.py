from random import seed, randint
from enum import Enum
import time


class RandomArray(Enum):

    #INFO: [How many values, min, max]
    SMALL = [10,0,100]
    MEDIUM = [100,0,1000]
    LARGE = [1000,0,10000]

    @staticmethod
    def generate(size,seed_val=time.time()):
        seed(seed_val)
        array = []

        for index in range(0,size[0],1):
            array.append(randint(size[1],size[2]))

        return array

# print(RandomArray.generate(RandomArray.SMALL.value))