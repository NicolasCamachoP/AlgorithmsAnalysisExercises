def max_subarray(numbers):

    """Find a contiguous subarray with the largest sum."""

    best_sum = 0  # or: float('-inf')

    best_start = best_end = 0  # or: None

    current_sum = 0

    for current_end, x in enumerate(numbers):

        if current_sum <= 0:

            # Start a new sequence at the current element

            current_start = current_end

            current_sum = x

        else:

            # Extend the existing sequence with the current element

            current_sum += x


        if current_sum > best_sum:

            best_sum = current_sum

            best_start = current_start

            best_end = current_end + 1  # the +1 is to make 'best_end' exclusive


    return best_sum, best_start, best_end
def Kadane(S):
    a = 0
    b = 0
    for x in S:
        b = b + x
        if b<0:
            b = 0
        if a < b:
            a = b
    return a        
    
#End def


S = [-1, -2, 1, 2, -2, 40]
print(max_subarray(S))
print(Kadane(S))