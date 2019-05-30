class Nodo:
        def __init__(self, valor, hijos = []):
            self.valor = valor
            self.hijos = hijos

def crear(m,x,y,a=[]):
    try:
        if (m[x][y]=='0' or m[x][y]=='x') and [x,y] not in a:
            return Nodo(m[x][y],[crear(m,x+1,y,a+[[x,y]])]+[crear(m,x-1,y,a+[[x,y]])]+[crear(m,x,y+1,a+[[x,y]])]+[crear(m,x,y-1,a+[[x,y]])])
        elif m[x][y]=='y':
            return Nodo('y')
	return None
    except IndexError:    
        return None

def hallar_x(matriz,iteracion=0):
	if 'x' in matriz[0]:
		return [iteracion,matriz[0].index('x')]
	return hallar_x(matriz[1:],iteracion+1)


def hallar(arbol, valor):
            if arbol == None:
                    return False
            elif arbol.valor == valor:
                    return True
            else:
                    return hallar_Hijos(arbol.hijos, valor)

def hallar_Hijos(lista, valor):
            if lista == []:
                    return False
            else:
                    return hallar(lista[0], valor) or hallar_Hijos(lista[1:], valor)


m=[x.split() for x in open('mapa.txt').readlines()]

i=hallar_x(m)
x,y=i

c=crear(m,x,y)

print(hallar(c,'y'))
