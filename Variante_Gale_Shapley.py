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
    #Usar diccs para ver las bandas y recitales que se juntan y quedan libres
    
def main():
    '''try:
        N, M, X, Y  = obtener_valores()
    except:
        print ("No ha ingresado los 4 numeros necesarios. El programa ha finalizado.")
        exit() '''
    N, M, X, Y = 10, 5, 2, 2
    generar_archivos(N, M)
    recitales_preferencias, bandas_preferencias = leer_archivos(N, M)
    variante_Gale_Shapley(recitales_preferencias, bandas_preferencias, X, Y)
    print("Fin del programa")
    

main()

    
N = 3 #recitales
M = 3 #bandas




            
    
