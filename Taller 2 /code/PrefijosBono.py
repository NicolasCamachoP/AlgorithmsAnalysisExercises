def Prefijo2(Sa,Sb):
    end = min(len(Sa),len(Sb))
    prefijo = ''
    for i in range(0,end):
        if Sa[i] == Sb[i]:
            prefijo += Sa[i]
        else:
            break
        #end if
    #end for
    return prefijo
#end def

def Prefijo_Aux(S, b, e):
    if b==e:
        return S[b]
    else:
        m = (b + e) // 2
        return Prefijo2( Prefijo_Aux( S, b, m), Prefijo_Aux( S, m + 1, e))
    #end if
#end def

def Prefijo(S):
    return Prefijo_Aux(S, 0, len(S) - 1)
#end def



S = ['Cacorro', 'Cacabsdf', 'Cacota','Cacorroea','Cacorris', 'Caco','Casa','Comedor','Hola']
print(Prefijo(S))

