def PolynomialPrinting(*polynoms):
	size = 0
	for poly in polynoms:
		size = len(poly)
		for i in range(size):
			print(poly[i], end = "")
			if (i != 0): 
				print("x^"+ str(i), end = ""); 
			if (i != size - 1): 
				print(" +  ", end = "");
			#End if
		#End for
		print(" ") 
	#End for
#End def
		


def NaivePolyMultiply(polyA, polyB):
	sizeA = len(polyA)
	sizeB = len(polyB)
	product = [0]*(sizeA + sizeB - 1)
	for i in range(sizeA):
		for j in range(sizeB):
			product[i + j] = product[i + j] + polyA[i] * polyB[j]
		#End for
	#End for
	return product 
#End def


def DAQPolyMultiply(A, B, Product):
	n  = len(polyA)
	A0 = [polyA[i] for i in range(n//2)]
	//B0 = []
	PolynomialPrinting(A0)
	
DAQPolyMultiply([1,10,6,-4,5],[1])
