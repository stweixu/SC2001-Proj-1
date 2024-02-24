from json import load
from MergeInsertionSort import mergeInsertionSort
from time import perf_counter
import numpy as np
import pandas as pd

def extractData(i):
    with open(f'data{i}.txt', 'r') as file:
        return load(file)


def mergeInsertionSortTimer(S, array):
    start = perf_counter()
    mergeInsertionSort(S, array, 0, len(array) - 1)
    return perf_counter() - start


def getResult(iteration):
    result = []

    for i in range(1, 5):
        array = extractData(f'data{1000 * (10**i)}.txt')
        for S in range(41):
            timeSum = 0
            for _ in range(iteration):
                arrayCopy = array.copy()
                timeSum += mergeInsertionSortTimer(S, arrayCopy)

            result.append(timeSum / iteration)
            print(f'S: {S}, Time: {result[-1]}')

        return result


def runTest(iteration):
    header = ['N = 1,000', 'N = 10,000', 'N = 100,000', 'N = 1,000,000', 'N = 10,000,000']
    result = np.asarray(getResult(extractData(i), iteration))

    pd.DataFrame(result).to_csv('Result_c_iii.csv', index_label='S', header=header)

runTest(50)

