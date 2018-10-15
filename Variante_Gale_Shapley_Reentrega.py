import sys,manejo_archivos_reentrega, heapq

#N = Cantidad de recitales
#M = Cantidad de bandas
#X = Cantidad de bandas que pueden contratar los recitales
#Y = Cantidad de recitales en los que puede participar una banda.
    
def variante_Gale_Shapley(recitales_preferencias, bandas_preferencias_pref_recital, bandas_preferencias_recital_pref, X, Y):
    recitales_libres = []
    bandas_por_recital = {}
    recitales_por_banda = {}
    for i in range(1, N+1): #O(N)
        recitales_libres.append(i)
        bandas_por_recital[i] = {}
    for j in range(1, M+1):     #O(M)
        recitales_por_banda[j] = [] #heap
    recitales_ult_propuesto = [0] * N
    
    while len(recitales_libres)>0: #O(N)
        recital_act = recitales_libres.pop() #O(1)
        for i in range(recitales_ult_propuesto[recital_act-1], M): #O(M)
            banda_act = recitales_preferencias[recital_act][i] 
            if len(bandas_por_recital[recital_act]) == X:
                break
            if len(recitales_por_banda[banda_act]) < Y: #Entonces se agrega al heap de la banda actual el recital actual.
                prioridad = bandas_preferencias_recital_pref[banda_act][recital_act] + 1 # + 1 para evitar dividir por 0. Para obtener la prioridad le resto 1.
                prioridad_en_el_heap = 1/(float(prioridad))
                heapq.heappush(recitales_por_banda[banda_act], prioridad_en_el_heap) #O(log(Y))
                bandas_por_recital[recital_act][banda_act] = True #El valor no tiene relevancia, lo importante es que remover la banda sea O(1).
            elif banda_prefiere_recital_nuevo(banda_act, recital_act, recitales_por_banda, bandas_preferencias_recital_pref): #O(1)
                recital_viejo = reemplazar_recital_viejo_por_nuevo(banda_act, recital_act, recitales_por_banda, bandas_por_recital, bandas_preferencias_recital_pref, bandas_preferencias_pref_recital) #O(log(Y))
                if recitales_ult_propuesto[recital_viejo-1] < M:
                    recitales_libres.append(recital_viejo)
            recitales_ult_propuesto[recital_act-1] += 1
    
    imprimir_resultados(bandas_por_recital)
    

def banda_prefiere_recital_nuevo(banda_act, recital_act, recitales_por_banda, bandas_preferencias_recital_pref):  #O(1)
    recital_con_menor_prioridad = recitales_por_banda[banda_act][0]
    prioridad_recital_nuevo = bandas_preferencias_recital_pref[banda_act][recital_act] + 1
    prioridad_recital_nuevo_heap = 1/(float(prioridad_recital_nuevo))
    if recital_con_menor_prioridad < prioridad_recital_nuevo_heap:
        return True
    return False
    
    
def reemplazar_recital_viejo_por_nuevo(banda_act, recital_act, recitales_por_banda, bandas_por_recital, bandas_preferencias_recital_pref, bandas_preferencias_pref_recital):#O(log(Y))
    prioridad_heap_recital_viejo = heapq.heappop(recitales_por_banda[banda_act]) 
    prioridad_recital_viejo = 1/(float(prioridad_heap_recital_viejo)) - 1
    recital_viejo = bandas_preferencias_pref_recital[banda_act][prioridad_recital_viejo]
    
    prioridad_recital_nuevo = bandas_preferencias_recital_pref[banda_act][recital_act] + 1
    prioridad_recital_nuevo_heap = 1/(float(prioridad_recital_nuevo))
    heapq.heappush(recitales_por_banda[banda_act], prioridad_recital_nuevo_heap) #O(log(Y))
    
    del bandas_por_recital[recital_viejo][banda_act] #O(log(Y))
    bandas_por_recital[recital_act][banda_act] = True
    return recital_viejo


def imprimir_resultados(bandas_por_recital):
    print("Recital | Bandas que tocan")
    print("--------------------------")
    for recital in bandas_por_recital:
        print("   {}    | {}".format(recital, bandas_por_recital[recital].keys()))


#En recitales_preferencias las claves son los numeros de preferencia y los valores las bandas, porque se deben recorrer las bandas en orden de preferencia
#En bandas_preferencias_pref_recital las claves son los numeros de preferencia y los valores los recitales, porque el heap guarda preferencias, y obtengo el recital que corresponde a cada preferencia con este diccionario en O(1)
#En bandas_preferencias_recital_pref las claves son los recitales y los valores los numeros de preferencia, porque se necesita guardar la preferencia segun el valor del recital.
def main(N,M,X,Y):
    manejo_archivos_reentrega.generar_archivos(N, M) #O(M+N)
    recitales_preferencias, bandas_preferencias_pref_recital, bandas_preferencias_recital_pref = manejo_archivos_reentrega.leer_archivos(N, M)
    variante_Gale_Shapley(recitales_preferencias, bandas_preferencias_pref_recital, bandas_preferencias_recital_pref, X, Y)
    print("Fin del programa")

    

if len(sys.argv)!=5:
    print("Se deben ingresar los cuatro parametros: N, M, X e Y")
    exit()
try:
    N = int(sys.argv[1])
    M = int(sys.argv[2])
    X = int(sys.argv[3])
    Y = int(sys.argv[4])
except ValueError:
    print("Se deben ingresar 4 valores numericos")
    exit()


main(N,M,X,Y)    

