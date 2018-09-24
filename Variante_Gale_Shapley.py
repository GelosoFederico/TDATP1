import sys,manejo_archivos

#N = Cantidad de recitales
#M = Cantidad de bandas
#X = Cantidad de bandas que pueden contratar los recitales
#Y = Cantidad de recitales en los que puede participar una banda.
    
def variante_Gale_Shapley(recitales_preferencias, bandas_preferencias, X, Y):
	recitales_libres = []
	bandas_por_recital = {}
	recitales_por_banda = {}
	for i in range(1, N+1): #O(N)
		recitales_libres.append(i)
		bandas_por_recital[i] = [] 
	for j in range(1, M+1):	 #O(M)
		recitales_por_banda[j] = []
	recitales_ult_propuesto = [0] * N
	
	while len(recitales_libres)>0: #O(N)
		recital_act = recitales_libres.pop() #O(1)
		for i in range(recitales_ult_propuesto[recital_act-1], M): #O(M)
			banda_act = recitales_preferencias[recital_act][i]
			if len(bandas_por_recital[recital_act]) == X:
				break
			if len(recitales_por_banda[banda_act]) < Y:
				recitales_por_banda[banda_act].append(recital_act)
				bandas_por_recital[recital_act].append(banda_act)
			elif banda_prefiere_recital_nuevo(banda_act, recital_act, recitales_por_banda, bandas_preferencias): #O(Y^2)
				recital_viejo = reemplazar_recital_viejo_por_nuevo(banda_act, recital_act, recitales_por_banda, bandas_por_recital, bandas_preferencias)#O(Y^2)
				if recitales_ult_propuesto[recital_viejo-1] < M:
					recitales_libres.append(recital_viejo)
			recitales_ult_propuesto[recital_act-1] += 1
	
	imprimir_resultados(bandas_por_recital)
	

def banda_prefiere_recital_nuevo(banda_act, recital_act, recitales_por_banda, bandas_preferencias):  #O(Y^2)
	for x in range(len(bandas_preferencias[banda_act])-1, 0, -1): #O(Y)
		if bandas_preferencias[banda_act][x] in recitales_por_banda[banda_act]: #O(Y)
			return True
		if bandas_preferencias[banda_act][x] == recital_act:
			return False
	
	
def reemplazar_recital_viejo_por_nuevo(banda_act, recital_act, recitales_por_banda, bandas_por_recital, bandas_preferencias):#O(Y^2)
	for x in range(len(bandas_preferencias[banda_act])-1, 0, -1): #O(Y)
		if bandas_preferencias[banda_act][x] in recitales_por_banda[banda_act]: #O(Y)
			recital_viejo = bandas_preferencias[banda_act][x]
			recitales_por_banda[banda_act].remove(recital_viejo)
			recitales_por_banda[banda_act].append(recital_act)
			bandas_por_recital[recital_viejo].remove(banda_act)
			bandas_por_recital[recital_act].append(banda_act)
			return recital_viejo


def imprimir_resultados(bandas_por_recital):
	print("Recital | Bandas que tocan")
	print("--------------------------")
	for x in range(1, len(bandas_por_recital)+1):
		print("   {}    | {}".format(x, bandas_por_recital[x]))

    
def main(N,M,X,Y):
    manejo_archivos.generar_archivos(N, M)
    recitales_preferencias, bandas_preferencias = manejo_archivos.leer_archivos(N, M)
    variante_Gale_Shapley(recitales_preferencias, bandas_preferencias, X, Y)
    print("Fin del programa")

	
	
if len(sys.argv)!=5:
	print("Se deben ingresar los cuatro parametros: N, M, X e Y")
	exit()
try:
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    X = int(sys.argv[3])
    Y =	int(sys.argv[4])
except ValueError:
	print("Se deben ingresar 4 valores numericos")
	exit()

main(N,M,X,Y)	

