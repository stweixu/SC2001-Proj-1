from json import load
from MergeInsertionSort import mergeInsertionSort
from time import perf_counter
import numpy as np
import pandas as pd

def extractData(i):
    with open(f'data{1000 * (10 ** i)}.txt', 'r') as file:
        return load(file)


def mergeInsertionSortTimer(S, array):
    start = perf_counter()
    mergeInsertionSort(S, array, 0, len(array) - 1)
    return perf_counter() - start


def getResult(array, iteration):
    result = []

    for S in range(41):
        timeSum = 0
        for _ in range(iteration):
            arrayCopy = array.copy()
            timeSum += mergeInsertionSortTimer(S, arrayCopy)

        result.append(timeSum / iteration)
        print(f'S: {S}, Time: {result[-1]}')
    
    return result


def runTest(i, iteration):
    header = [['N = 100,000'], ['N = 10,000'], ['N = 100,000'], ['N = 1,000,000'], ['N = 10,000,000']]

    result = np.asarray(getResult(extractData(i), iteration))
    pd.DataFrame(result).to_csv(f'Result_c_iii_{i}.csv', index_label = 'S', header = header[i])


# Do not run unless you are sure you want to overwrite the file
# runTest(0, 50)
# runTest(1, 50)
# runTest(2, 50)
# runTest(3, 50)
# runTest(4, 50)
