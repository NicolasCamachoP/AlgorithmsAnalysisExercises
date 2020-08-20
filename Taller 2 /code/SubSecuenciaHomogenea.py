def SimpleMaxSubArrayv2(S):
    n = 0
    nAux = 1
    subArray = []
    subArrayAux = []
    for j in range (1, len(S)):
        if S[j] == S[j-1]:
            if nAux == 1:
                subArrayAux.append(S[j-1])
                subArrayAux.append(S[j])
                nAux += 1
            else:
                subArrayAux.append(S[j])
                nAux += 1
            #end if
        else:
            if nAux >= n:
                subArray = subArrayAux[:nAux]
                n = nAux        
            subArrayAux = []
            nAux = 1
        #end if
    #end for
    return subArray
#end def

def FindMaxHomCrossSubArray(array, low, mid, high):
    maxRight = -1
    maxLeft = -1
    leftSum = float('-inf')
    sum = 0
    for i in range(mid, low - 1, -1):
        if array[i] == array[i + 1]:
            sum = sum + 1
        else:
            sum  = 0
            pass
        if sum >= leftSum:
            leftSum = sum
            maxLeft = i
            # end if
        #end if
    # end for
    rightSum = float('-inf')
    sum = 0
    for j in range(mid + 1, high + 1):
        if array[j] == array[j - 1]:
            sum = sum + 1
        else:
            sum = 0
            pass
        if sum >= rightSum:
            rightSum = sum
            maxRight = j
            # end if
        #end if
    # end for
    return maxLeft, maxRight, leftSum + rightSum
# end def


def FindMaximunHomSubarray(array, low, high):
    if high <= low:
        return low, high, 1
    else:
        mid = (low + high) // 2
        leftLow, leftHigh, leftSum = FindMaximunHomSubarray(array, low, mid)
        rightLow, rightHigh, rightSum = FindMaximunHomSubarray(array, mid + 1, high)
        crossLow, crossHigh, crossSum = FindMaxHomCrossSubArray(array, low, mid, high)
        if leftSum >= rightSum and leftSum >= crossSum:
            return leftLow, leftHigh, leftSum
        elif rightSum >= leftSum and rightSum >= crossSum:
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum
        # end if
    # end if
# end def


S = ['a','a','a','a','a','b','b','b','b','b','b',
     'b','b','b','b','c','c','c','c','c','c','c','c'
    ,'c','c','c','c','c','c','c','c','c','c','c','c'
    ,'c','c','c','c','c','c','c','w','e','w','e','l'
    ,'j',2,'o','l','i',2]
Sprima1 = SimpleMaxSubArrayv2(S)
print(f'Según el algoritmo ingenuo, el máximo sub arreglo está conformado por {len(Sprima1)} "{Sprima1[0]}"  y es:\n{Sprima1}')
low, high, suma = FindMaximunHomSubarray(S, 0, len(S) - 1)
print(f'Según el algoritmo dividir-y-vencer, el máximo sub arreglo está  conformado por {suma} "{S[low]}" y es:\n{S[low:high + 1]}')
