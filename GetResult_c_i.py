from json import load, dump
from MergeInsertionSort import mergeInsertionSort
import numpy as np
import pandas as pd


def generateIndex():
    array = []
    N = 1000
    for _ in range(4):
        for i in range(1, 10, 2):
            array.append(N * i)
        N *= 10

    array.append(10000000)
    return array


def runTest():
    result = []

    for i in range(4):
        with open(f'datarange{1000 * (10 ** i)}.txt', 'r') as file:
            dataset = load(file)

        for array in dataset:
            result.append(mergeInsertionSort(10, array, 0, len(array) - 1))

    with open('data10000000.txt', 'r') as file:
        result.append(mergeInsertionSort(10, load(file), 0, 9999999))

    df = pd.DataFrame(np.asarray(result)).set_index(pd.Index(generateIndex()))
    df.to_csv('Result_c_i.csv', index_label = 'N', header = ['Key Comparison'])