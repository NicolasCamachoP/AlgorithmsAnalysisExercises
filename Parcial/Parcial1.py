from math import factorial
def CountAditiveRangesAux(array, b, e, rango):
    if b == e:
        if array[b] in range(rango[0] + 1, rango[1]):
            return 1
        else:
            return 0
    else:
        q = (e+b)//2
        totalIzq = CountAditiveRangesAux(array, b, q, rango)
        totalDer = CountAditiveRangesAux(array, q + 1, e, rango)
        return totalIzq + totalDer
# end def

def CountAditiveRanges(array, rango):
    total = CountAditiveRangesAux(array, 0, len(array)-1, rango)
    return Combinatoria(total, 2) + total
def Combinatoria(n, x):
    return factorial(n)//(factorial(x)*factorial(n-x))

S = [-12, 4, -30, 100, 5, 1, 2]
rango = [-10, 6]
total = CountAditiveRanges(S,rango)
print(f'El núnero de rangos aditivos es {total}')