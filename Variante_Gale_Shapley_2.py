import random

#N = Cantidad de recitales
#M = Cantidad de bandas
#X = Cantidad de bandas que pueden contratar los recitales
#Y = Cantidad de recitales en los que puede participar una banda.

def obtener_valores():
    numeros = raw_input("A continuacion Ingrese los valores numericos enteros N, M, X e Y: ")
    N, M, X, Y = map(int, numeros.split())
    return N, M, X, Y

#Genera N archivos de recital con sus preferencias en forma random, y M archivos para las bandas con sus preferencias random.
def generar_archivos(N, M):
    for i in range(N):
        recital_nro = 'recital_' +  str(i+1) + '.txt'
        with open(recital_nro, 'w+') as recital:
            recital_preferencias = random.sample(range(1, M + 1), M)
            for preferencia in recital_preferencias:
                recital.write(str(preferencia))
                recital.write(str('\n'))
    for i in range(M):
        banda_nro = 'banda_' +  str(i+1) + '.txt'
        with open(banda_nro, 'w+') as banda:
            banda_preferencias = random.sample(range(1, N + 1), N)
            for preferencia in banda_preferencias:
                banda.write(str(preferencia))
                banda.write(str('\n'))

#Retorna 2 diccionarios con las preferencias de los recitales y las bandas.
def leer_archivos(N, M):
    recitales_preferencias = {}
    for i in range(1, N + 1):
        recital_nro = 'recital_' +  str(i) + '.txt'
        recital_preferencias = []
        with open(recital_nro, 'r') as recital:
            for preferencia in range(M):
                recital_preferencias.append(int(recital.readline()))
        recitales_preferencias[i] = recital_preferencias
    bandas_preferencias = {}
    for i in range(1, M + 1):
        banda_nro = 'banda_' +  str(i) + '.txt'
        banda_preferencias = []
        with open(banda_nro, 'r') as banda:
            for preferencia in range(N):
                banda_preferencias.append(int(banda.readline()))
        bandas_preferencias[i] = banda_preferencias
    return recitales_preferencias, bandas_preferencias
    
def variante_Gale_Shapley(recitales_preferencias, bandas_preferencias, X, Y):
    bandas = list(bandas_preferencias.keys())
    recitales_libres = list(recitales_preferencias.keys())
    recitales_matcheos = {}
    for recital in recitales_libres:
        recitales_matcheos[recital] = []
    bandas_matcheos = {}
    for banda in bandas:
        bandas_matcheos[banda] = []
    recital = recitales_libres[len(recitales_libres) - 1] #inicializacion
    while (len(recitales_libres) > 0) and (len(recitales_preferencias[recital]) > 0): #Mientras haya un postulante libre y el postulante libre no se haya postulado a todas las bandas (A medida que avanza el while voy sacando bandas de las preferenciasw de los recitales, total se postulan 1 sola vez).
        recital = recitales_libres[len(recitales_libres) - 1] #Extraer el ultimo elemnto es O(1)
        #if (len(recitales_preferencias[recital]) > 0): #Y el postulante libre no se haya postulado a todas las bandas (A medida que avanza el while voy sacando bandas de las preferenciasw de los recitales, total se postulan 1 sola vez).
        banda_preferida_actual = recitales_preferencias[recital].pop(0) #recitales_preferencias[recital][0] es la mejor banda a la que el recital no se postulo todavia, y solo se puede postular 1 vez a cada banda. (Es O(n)).
        if len(bandas_matcheos[banda_preferida_actual]) < Y: #bandas_matcheos son los recitales a los que va cada banda y si son menor a Y puede ir a una banda mas al menos.
            bandas_matcheos[banda_preferida_actual].append(recital)
            recitales_matcheos[recital].append(banda_preferida_actual) #Si la banda esta libre (o sea tiene lugar para uno mas), la agrego al matcheo.
            if len(recitales_matcheos[recital]) == X:
                recitales_libres.remove(recital) #Extraer el ultimo elemnto es O(1)
        else: #La banda ya matcheo con Y recitales
            pos_preferencia_del_recital_actual = bandas_preferencias[banda_preferida_actual].index(recital)
            pos_recital_menor_preferencia = 0
            pos_menor = 0
            for j in range(len(bandas_matcheos[banda_preferida_actual])) :
                '''Los recitales no se agregan en orden de preferencia, entonces tengo que buscar entre todos y compararlos para ver cual es el menos preferido '''
                pos_prefencia_del_recital_matcheado = bandas_preferencias[banda_preferida_actual].index(bandas_matcheos[banda_preferida_actual][j]) #Busco los indices en la lista de preferencias de la banda, para ver cual es el recital con menor preferencia para reemplazarlo en caso que sea menor al nuevo recital.
                if pos_recital_menor_preferencia < pos_prefencia_del_recital_matcheado: 
                    pos_recital_menor_preferencia = pos_prefencia_del_recital_matcheado #pos_recital_menor_preferencia terminara siendo la posicion del recital con menor preferencia dentro de los recitales que habian matcheado con la banda preferida actual del nuevo recital.
                    pos_menor = j
            if pos_preferencia_del_recital_actual < pos_recital_menor_preferencia: #La banda prefiere al nuevo recital por sobre los que tenia
                recital_viejo = bandas_matcheos[banda_preferida_actual][pos_menor]
                recitales_matcheos[recital_viejo].remove(banda_preferida_actual)
                if recital_viejo not in recitales_libres:
                    recitales_libres.append(recital_viejo) #El recital que habia sido matcheado debera buscar una nueva banda, bajando sus preferencias
                bandas_matcheos[banda_preferida_actual].remove(recital_viejo) #Extraigo el viejo recital de los matcheos de la banda.
                bandas_matcheos[banda_preferida_actual].append(recital) #Incluyo el nuevo recital
                recitales_matcheos[recital].append(banda_preferida_actual) 
                if len(recitales_matcheos[recital]) == X:
                    recitales_libres.remove(recital) #Extraer el ultimo elemnto es O(1)
            #else: #la banda prefiere a los recitales que ya tiene, por lo tanto el recital actual sigue libre, y pasa a la siguiente banda de sus preferencias.
    return recitales_matcheos
                        
                        
    
def main():
    try:
        N, M, X, Y  = obtener_valores()
    except:
        print ("No ha ingresado los 4 numeros necesarios. El programa ha finalizado.")
        exit()
    #N, M, X, Y = 10,5,2,2
    generar_archivos(N, M)
    recitales_preferencias, bandas_preferencias = leer_archivos(N, M)
    print recitales_preferencias, '\n', bandas_preferencias
    print (variante_Gale_Shapley(recitales_preferencias, bandas_preferencias, X, Y))
    print("Fin del programa")
    

main()

 
