import random

#N = Cantidad de recitales
#M = Cantidad de bandas
#X = Cantidad de bandas que pueden contratar los recitales
#Y = Cantidad de recitales en los que puede participar una banda.

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

def leer_archivos(N, M):
    recitales_preferencias = {} #Las claves son los numeros de preferencia y los valores las bandas, porque se deben recorrer las bandas en orden de preferencia
    for i in range(1, N + 1):
        recital_nro = 'recital_' +  str(i) + '.txt'
        recital_preferencias = {} #Linea cambiada
        with open(recital_nro, 'r') as recital:
            for j in range(M):
                recital_preferencias[j] = int(recital.readline()) #Linea cambiada
        recitales_preferencias[i] = recital_preferencias
        
    bandas_preferencias_pref_recital = {}#las claves son los numeros de preferencia y los valores los recitales, porque el heap guarda preferencias, y obtengo el recital que corresponde a cada preferencia con este diccionario en O(1)
    for i in range(1, M + 1):
        banda_nro = 'banda_' +  str(i) + '.txt'
        banda_preferencias = {} #Linea cambiada
        with open(banda_nro, 'r') as banda:
            for j in range(N):
                banda_preferencias[j] = int(banda.readline())  #Linea cambiada
        bandas_preferencias_pref_recital[i] = banda_preferencias
        
    bandas_preferencias_recital_pref = {}#las claves son los recitales y los valores los numeros de preferencia, porque se necesita guardar la preferencia segun el valor del recital.
    for i in range(1, M + 1):
        banda_nro = 'banda_' +  str(i) + '.txt'
        banda_preferencias = {} #Linea cambiada
        with open(banda_nro, 'r') as banda:
            for j in range(N):
                banda_preferencias[int(banda.readline())] = j #Linea cambiada
        bandas_preferencias_recital_pref[i] = banda_preferencias
        
    return recitales_preferencias, bandas_preferencias_pref_recital, bandas_preferencias_recital_pref


