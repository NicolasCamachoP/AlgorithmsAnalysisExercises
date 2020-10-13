import math

#Naive aproach
def APNaive(V, O):
    return max(APNaive_Aux(V, O, 0, len(V)))

#End def
def APNaive_Aux(V, O, a, b):
    if a==b:
        if a >= len(V): return [V[a - 1], V[a - 1]]
        print(f"Valió en a: {a} b: {b} V[a]: {V[a]}")
        return [V[a], V[a]]
    else:
        q = [math.inf, -math.inf]
        for i in range(a, b):
            l = APNaive_Aux(V, O, a, i)
            r = APNaive_Aux(V, O, i + 1, b)
            print(f"i: {i} a:{a} b:{b}")
            print(f"L: {l}")
            print(f"R: {r}")
            if i != b - 1:
                if (i == 1): print("SI LO HACE ")
                print(i)
                smm = eval(str(l[0]) + O[i] + str(r[0]))
                smx = eval(str(l[0]) + O[i] + str(r[1]))
                sxm = eval(str(l[1]) + O[i] + str(r[0]))
                sxx = eval(str(l[1]) + O[i] + str(r[1]))
                S = [min(smm, smx, sxm, sxx), max(smm, smx, sxm, sxx)]
            else:
                S = [V[a], V[a]]
            print(S)
            if S[0] < q[0]:
                q[0] = S[0]
            #End if
            if S[1] > q[1]:
                q[1] = S[1]
            #End if
        #End for
        return q
    #End if
#End def
V = [1, 2, 3, 4, 5]
O = ["+", "-", "*", "-"]
sol = APNaive(V, O)
print(f"Solution: {sol}")