from random import sample
from json import dump


# Generate a .txt file that contains an arrays of 5 randomly sorted list in increasing size.
# If N is 1000, this will generate 5 arrays of 1000, 3000, 5000, 7000, 9000.
def generateRange(N, name):
    data = []

    for i in range(1, 10, 2):
        maxNum = N * i * 10 - 1
        data.append(sample(range(1, maxNum), N * i))
        # random.sample(list L, size N) returns a randomly sorted sub-list
        # of size N from input list L

    with open(name, 'w') as file:
        dump(data, file)


# Generate a .txt file that contains 1 randomly sorted list of N size
def generateNData(N, name):
    data = []
    maxNum = N * 10 - 1
    for i in range(10):
        data.append(sample(range(1, maxNum), N))
    with open(name, 'w') as file:
        dump(data, file)


for i in range (1,101):
    generateNData(i, f'data{i}.txt')

# generateRange(1000, 'datarange1000.txt')
# generateRange(10000, 'datarange10000.txt')
# generateRange(100000, 'datarange100000.txt')
# generateRange(1000000, 'datarange1000000.txt')

# generateNData(1000, 'data1000.txt')
# generateNData(10000, 'data10000.txt')
# generateNData(100000, 'data100000.txt')
# generateNData(1000000, 'data1000000.txt')
# generateNData(10000000, 'data10000000.txt')
