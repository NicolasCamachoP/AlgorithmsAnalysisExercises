def SequenceFileReader(fileName):
    sequence = []
    with open(fileName) as file:
        for line in file:
            sequence.append([int(x) for x in line.split()][0])
        # end for
    # end with
    return sequence


# end def


## -------------------------------------------------------------------------
## BinSearch: search the index of a value in an ordered sequence of comparable (<) elements
## @inputs: sequence, a reference to a secuence of comparable elements.
##          value, value of wich an index is searched.
##          start, start of the subsequence.
##          end, end of the subsequence.
## @outputs: index, the index of de value if found or -1.
## -------------------------------------------------------------------------
def BinSearch(sequence, value, start, end):
    if end < start:
        return -1
    else:
        index = (start + end) // 2
        if sequence[index] < value:
            return BinSearch(sequence, value, index + 1, end)
        elif value < sequence[index]:
            return BinSearch(sequence, value, start, index - 1)

        else:
            return index
        # end if
    # end if
# end def


## -------------------------------------------------------------------------
## MergeSort: search the index of a value in an ordered sequence of comparable (<) elements
## @inputs: sequence, a reference to a secuence of comparable elements.
##          value, value of wich an index is searched.
##          start, start of the subsequence.
##          end, end of the subsequence.
## @outputs: index, the index of de value if found or -1.
## -------------------------------------------------------------------------
def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2
        MergeSort(array, start, mid)
        MergeSort(array, mid + 1, end)
        Merge(array, start, mid, end)
    #end if
#end def


## -------------------------------------------------------------------------
## Merge: search the index of a value in an ordered sequence of comparable (<) elements
## @inputs: sequence, a reference to a secuence of comparable elements.
##          value, value of wich an index is searched.
##          start, start of the subsequence.
##          end, end of the subsequence.
## @outputs: index, the index of de value if found or -1.
## -------------------------------------------------------------------------
def Merge(array, start, mid, end):
    n1 = mid - start + 1
    n2 = end - mid
    L = []
    R = []
    for i in range(0, n1 + 1):
        L.append(array[start + i - 1])
    #end for
    for j in range(0, n2 + 1):
        R.append(array[mid + j])
    #end for
    L.append(float('inf'))
    R.append(float('inf'))
    i = 1
    j = 1
    for k in range(start, end + 1):
        if L[i] <= R[j]:
            array[k] = L[i]
            i += 1
        else:
            array[k] = R[j]
            j += 1
        #end if
    #end for
#end def


## -------------------------------------------------------------------------
## FindMaxCrossSubArray: search the sub array wich sum is the biggest
## @inputs: array, an array reference to an array of items summable with operator (+)
##          low, the start index of the array.
##          mid, the mid index of the array.
##          end, the end index of the array.
## @outputs: maxLeft, the start index of the found subarray.
##           maxRight, the end index of the found subarray.
##           leftSum + rightSum, the total sum of the found subarray
## -------------------------------------------------------------------------
def FindMaxCrossSubArray(array, low, mid, high):
    maxRight = -1
    maxLeft = -1
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        sum = sum + array[i]
        if sum > leftSum:
            leftSum = sum
            maxLeft = i
        # end if
    # end for
    rightSum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        sum = sum + array[j]
        if sum > rightSum:
            rightSum = sum
            maxRight = j
        # end if
    # end for
    return maxLeft, maxRight, leftSum + rightSum


# end def

## -------------------------------------------------------------------------
## FindMaximunSubarray: search the sub array wich sum is the biggest
## @inputs: array, an array reference to an array of items summable with operator (+)
##          low, the start index of the array.
##          end, the end index of the array.
## @outputs: leftLow or rightLow or crossLow, the start index of the found subarray.
##           leftHigh or rightHigh or crossHigh, the end index of the found subarray.
##           leftSum or rightSum or crossSum, the total sum of the found subarray.
## -------------------------------------------------------------------------
def FindMaximunSubarray(array, low, high):
    if high <= low:
        return low, high, array[low]
    else:
        mid = (low + high) // 2
        leftLow, leftHigh, leftSum = FindMaximunSubarray(array, low, mid)
        rightLow, rightHigh, rightSum = FindMaximunSubarray(array, mid + 1, high)
        crossLow, crossHigh, crossSum = FindMaxCrossSubArray(array, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum
        # end if
    # end if


# end def


## -------------------------------------------------------------------------
## Main code
## -------------------------------------------------------------------------

##Binary search use
"""sequence = SequenceFileReader('python3_quick.txt')
value = int(input('Please enter a number betwen 0 - 9999: '))
index = BinSearch(sequence, value, 0, len(sequence) - 1)
if index == -1:
    print(f'The number {value} does not exist in python3_quick.txt')
else:
    print(f'The number {sequence[index]} is in the position {index}!')
"""
##Maximum sub array use
"""
price = [100, 113, 110, 85, 105, 102, 86, 63, 81, 101, 94, 106, 101,
         79, 94, 90, 97]
change = []
for i in range(1, len(price)):
    change.append(price[i] - price[i - 1])
print(len(change))
print(change)
low, high, suma = FindMaximunSubarray(change, 0, len(change) - 1)
print(f'Low: {low}, Right: {high}, Sum: {suma}')
"""
##Merge sort use
array = [x for x in range(30,0,-1)]
print(array)
MergeSort(array, 0, len(array)-1)
print(array)