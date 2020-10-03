def MaxDiff_Aux(A, i):
    if i == 0:
        return 0
    else:
        l = MaxDiff_Aux(A, i - 1) + A[i - 1]
        r = MaxDiff_Aux(A, i - 1) - A[i - 1]
        if abs( l ) < abs ( r ):
            return l
        else:
            return r
        #End if
    #End if
#End def

def MaxDiff(A):
    return MaxDiff_Aux(A, len(A))
#End def

print(MaxDiff([1,2,3,4,1000]))
    