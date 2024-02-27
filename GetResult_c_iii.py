from json import load
from MergeInsertionSort import *
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

def mergeSortTimer(array):
    start = perf_counter()
    mergeSort(array, 0, len(array) - 1)
    return (perf_counter() - start) * 10**6

def insertionSortTimer(array):
    start = perf_counter()
    insertionSort(array, 0, len(array) - 1)
    return (perf_counter() - start) * 10**6


def getResult(iteration):
    # iteration refers to number of times test was done. Higher iteration reduces outliers

    insertionSortResult =  []
    mergeSortResult = []

    for dataSize in range (1,101):
        array = extractData(dataSize)
        mergeSortTimeSum = 0
        insertionSortTimeSum = 0

        for index in range(len(array)):
            for _ in range(iteration):
                arrayCopyForMerge = array[index].copy()
                mergeSortTimeSum += mergeSortTimer(arrayCopyForMerge)

                arrayCopyForInsertion = array[index].copy()
                insertionSortTimeSum += insertionSortTimer(arrayCopyForInsertion)

        mergeSortResult.append(mergeSortTimeSum / len(array) * iteration)
        insertionSortResult.append(insertionSortTimeSum / len(array) * iteration)

    collatedResult = [insertionSortResult, mergeSortResult]

    return collatedResult


    # collated_result = []
    # for i in range(5):
    #     result = []
    #     data_size = 1000 * 10 ** i
    #     array = extractData(data_size)
    #     for S in range(41):
    #         timeSum = 0
    #         for _ in range(iteration):
    #             arrayCopy = array.copy()
    #             timeSum += mergeInsertionSortTimer(S, arrayCopy)
    #
    #         result.append(timeSum / iteration)
    #         print(f'Data = {data_size}, S: {S}, Time: {result[-1]}')
    #
    #     collated_result.append(result)
    # print(collated_result)
    # return collated_result


def runTest(iteration):
    header = ['Insertion Sort', 'MergeSort']
    result = (getResult(iteration))

    result = pd.DataFrame(result)
    pd.DataFrame.transpose(result).to_csv("Result_c_iii_updated.csv", index_label='S', header=header)


#     header = ['N = 1,000', 'N = 10,000', 'N = 100,000', 'N = 1,000,000', 'N = 10,000,000']
#     result = (getResult(iteration))
#
#     result = pd.DataFrame(result)
#     pd.DataFrame.transpose(result).to_csv("Result_c_iii.csv", index_label='S', header=header)
#
#
runTest(5)  # 5 iterations on the same list


