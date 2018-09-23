# -*- coding: utf-8 -*-
# TP1 TDA Parte 2: Complejidad algorítmica
# Obtener una lista de primos hasta el número N.
# Se puede hacer de dos métodos, con la criba de Erastótenes (llamando con E) o
# por fuerza bruta (llamando con F) 

import time
import argparse

def main(N,M):
    ## Lectura de command line
    #N = 100
    start_time = time.time()
    if M == "E":
        prime_list = primes_until_N_E(N)
    if M == "F":
        prime_list = primes_until_N_F(N)
    diff = time.time()-start_time
    print(prime_list)
    print(diff)


def primes_until_N_E( N ):
    # Devuelve una lista L con los primos hasta N.
    # Implementa la criba de Erastótenes
    if N == 1:
        return []
    if N == 2:
        return []
    primes = [True] * N;
    primes[0] = primes[1] = False;
    # Saco los pares para mejorar después la criba
    for i in range(4,N,2):
        primes[i] = False
    # Recorro los números y actúo para los impares, empezando desde el número al
    # cuadrado y moviéndome de a 2 en sus múltiplos, porque ya se que i*i es
    # impar, impar+impar es par y esos ya los descarté antes
    for i in range(1,N,2):
        if primes[i] == True:
            for j in range(i*i,N,2*i):
                primes[j] = False
    # Ahora formo la lista con los que quedaron
    final_primes = [2]
    for i in range(3,N,2):
        if primes[i] == True:
            final_primes.append(i)
    return final_primes

def primes_until_N_F( N ):
    # Devuelve una lista L con los primos hasta N.
    # Lo hace de forma Naive
    if N == 1:
        return []
    primes = []
    for i in range(2,N):
        isprime = True
        j = 2
        while isprime == True and j < i:
            if i%j==0:
                isprime = False
            j = j+1
        if isprime == True:
            primes.append(i)
    return primes



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser.')
    parser.add_argument('number',type=int)
    parser.add_argument('method',choices=['E', 'F'])
    parsed_args = parser.parse_args()
    N = parsed_args.number
    M = parsed_args.method
    if not M == "E" and not M == "F":
        print("Bad Method")
        quit()
    main(N,M)
