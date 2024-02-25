from json import load
from MergeInsertionSort import mergeSort, mergeInsertionSort
from time import perf_counter
import numpy as np
import pandas as pd


# iteration refers to number of times this test was done
# Repeating test improves result consistency and reduces outlier
def mergeSortTimer(array, iteration):

    timeSum = 0

    for _ in range(iteration):
        arrayCopy = array.copy()
        start = perf_counter()
        key = mergeSort(arrayCopy, 0, 9999999)
        timeSum += perf_counter() - start
    
    return [key, timeSum / iteration]


def mergeInsertionSortTimer(array, iteration, S):
    timeSum = 0

    for _ in range(iteration):
        arrayCopy = array.copy()
        start = perf_counter()
        key = mergeInsertionSort(S, arrayCopy, 0, 9999999)
        timeSum += perf_counter() - start
    
    return [key, timeSum / iteration]


def runTest(iteration, S):
    result = []

    with open('data10000000.txt', 'r') as file:
        array = load(file)

    result.append(mergeSortTimer(array, iteration))
    print(result[0])
    result.append(mergeInsertionSortTimer(array, iteration, S))
    print(result[1])
    df = pd.DataFrame(np.asarray(result)).set_index(pd.Index(['Original', 'Hybrid']))
    df.to_csv('Result_d.csv', header = ['Key Comparison', 'Time'])


runTest(5 , 10)