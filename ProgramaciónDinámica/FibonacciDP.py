#Naive
def Fibonacci(i):
    if i <= 1:
        return i
    else:
        return Fibonacci(i - 1) + Fibonacci(i - 2)
    #end if
#End def


#Memoizada
def Fibonacci_M(i, M):
    if M[i] == -1:    
        if i <= 1:
            M[i] = i
        else:
            M[i] =  Fibonacci_M(i - 1, M) + Fibonacci_M(i - 2, M)
        #end if
    #End if
    return M[i]
#End def
def FibonacciP(i):
    M = [-1 for j in range(i+1)]
    return Fibonacci_M(i, M)
#End def

#bottom-up
def FibonacciBU(i):
    M = [-1 for j in range(i+1)]
    M[0] = 0
    M[1] = 1
    for k in range(2, i + 1):
        M[k] = M[k - 1] + M[k - 2]
    #End for
    return M[i]
#End def


#Main 
f = FibonacciBU(20)
print(f)
f = FibonacciBU(40)
print(f)