#Iésimo elemento de la serie de fibonacci
#Caracterización recursiva de la solución recursiva mediante un algoritmo recursivo
  
def FibonacciNaive (indice):
    #Caso Base, cuando i es 1 o 0
    if indice <= 1:
        return indice
    #Definición recursiva
    else:
        return FibonacciNaive(indice - 1) + FibonacciNaive(indice - 2)
    #End if
#End def


#Memoización del algoritmo Naive
#Guardar valores ya calculados (M)
def FibonacciMemo(indice):
    #Crear Tabla para almacenar los datos
    M = [-1]*(indice+1)
    #Casos Base
    M[0] = 0
    M[1] = 1
    return FibonacciMemoAux(M, indice)
#End def
def FibonacciMemoAux (M,indice):
    #Verificar si el resultado ya está calculado 
    if M[indice] == -1:    
        #Si no está calculado, almacenar resultado
        #Caso Base, cuando i es 1 o 0
        if indice <= 1:
            M[indice] =  indice
        #Definición recursiva
        else:
            M[indice] = FibonacciMemoAux(M,indice - 1) + FibonacciMemoAux(M,indice - 2)
        #End if
    #End if
    #Si ya está calculado, devolver valor de la tabla
    return M[indice]
#End def


#Algoritmo Bottom-up
#Transformar la pila de recursión en una secuencia de llamadas
def FibonacciBottom(indice):
    #Crear Tabla para almacenar los datos
    M = [-1]*(indice+1)
    #Casos Base
    M[0] = 0
    M[1] = 1
    #Se utilizan los casos bases para llenar el resto de la tabla
    for i in range (2, indice + 1):
        M[i] = M[i-1] + M[i -2]
    return M[indice]
#End def


i = 35
print('Usando Algoritmo Evidente:')
print(f'El elemento número {i} en la secuencia Fibonacci es {FibonacciNaive(i)}')
print('Usando Algoritmo con memoización :')
print(f'El elemento número {i} en la secuencia Fibonacci es {FibonacciMemo(i)}')
print('Usando Algoritmo con bottom-up :')
print(f'El elemento número {i} en la secuencia Fibonacci es {FibonacciBottom(i)}')
