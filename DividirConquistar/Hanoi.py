def hanoi(n, i, a, e):
    if n <= 1:
        print("Move from", i, "to", e)
    else:
        hanoi(n - 1, i, e, a)
        print("Move from", i, "to", e)
        hanoi( n - 1, a, i, e)
    #End if
#End def

hanoi(4, 0, 1, 2)
