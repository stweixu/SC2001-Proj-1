from random import sample
from json import dump


def generateRange(N, name):     # generate data
    data = []
    for i in range(1, 10, 2):
        # if N is 1000, this will generate 5 arrays of 1000, 3000, 5000, 7000, 9000
        maxNum = N * i * 10 - 1

        data.append(sample(range(1, maxNum), N * i))
        # sample(list L, size N) returns a randomly sorted sub-list
        # of size N from input list L

    with open(name, 'w') as file:
        dump(data, file)


def generateNData(N, name):
    maxNum = N * 10 - 1
    data = sample(range(1, maxNum), N)
    with open(name, 'w') as file:
        dump(data, file)

# generateRange(1000, 'datarange1000.txt')
# generateRange(10000, 'datarange10000.txt')
# generateRange(100000, 'datarange100000.txt')
# generateRange(1000000, 'datarange1000000.txt')

# generateNData(1000, 'data1000.txt')
# generateNData(10000, 'data10000.txt')
# generateNData(100000, 'data100000.txt')
# generateNData(1000000, 'data1000000.txt')
# generateNData(10000000, 'data10000000.txt')
