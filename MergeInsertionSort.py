def insertionSort(array, left, right):
    comparisons = 0

    for i in range(left + 1, right + 1):
        key = array[i]
        j = i - 1

        while j >= left:
            comparisons += 1
            if array[j] <= key:
                break
            
            array[j+1] = array[j]
            j -= 1

        array[j+1] = key

    return comparisons


def merge(array, left, mid, right):
    i = j = comparisons = 0
    k = left
    sizeL = mid - left + 1
    sizeR = right - mid
    arrayL = array[left: mid + 1]
    arrayR = array[mid + 1: right + 1]

    while i < sizeL and j < sizeR:
        if arrayL[i] <= arrayR[j]:
            array[k] = arrayL[i]
            k += 1
            i += 1
        else:
            array[k] = arrayR[j]
            k += 1
            j += 1
        comparisons += 1

    while i < sizeL:
        array[k] = arrayL[i]
        k += 1
        i += 1
    
    while j < sizeR:
        array[k] = arrayR[j]
        k += 1
        j += 1
    
    return comparisons


def mergeInsertionSort(S, array, left, right):
    comparisons = 0

    if right == left:
        return 0
    
    if right - left < S:
        return insertionSort(array, left, right)
    
    mid = int((left + right) / 2)
    comparisons += mergeInsertionSort(S, array, left, mid)
    comparisons += mergeInsertionSort(S, array, mid + 1, right)
    comparisons += merge(array, left, mid, right)
    return comparisons


def mergeSort(array, left, right):
    comparisons = 0
    
    if right <= left:
        return 0
    
    mid = int((left + right) / 2)
    comparisons += mergeSort(array, left, mid)
    comparisons += mergeSort(array, mid + 1, right)
    comparisons += merge(array, left, mid, right)
    return comparisons