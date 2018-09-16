# -*- coding: utf-8 -*-
# TP1 TDA Parte 2: Complejidad algor�tmica
# Obtener una lista de primos hasta el n�mero N.
# Se puede hacer de dos m�todos, con la criba de Erast�tenes (llamando con E) o
# por fuerza bruta (llamando con F) 

import time
import argparse

def main(N,M):
    ## Lectura de command line
    #N = 100
    start_time = time.time_ns()
    if M == "E":
        prime_list = primes_until_N_E(N)
    if M == "F":
        prime_list = primes_until_N_F(N)
    diff = time.time_ns()-start_time
    # TODO que hago? Los imprimo?
    print(prime_list)
    print(diff)


def primes_until_N_E( N ):
    # Devuelve una lista L con los primos hasta N.
    # Implementa la criba de Erast�tenes
    if N == 1:
        return []
    if N == 2:
        return [2]
    primes = [True] * N;
    primes[0] = primes[1] = False;
    # Saco los pares para mejorar despu�s la criba
    for i in range(4,N,2):
        primes[i] = False
    # Recorro los n�meros y act�o para los impares, empezando desde el n�mero al
    # cuadrado y movi�ndome de a 2 en sus m�ltiplos, porque ya se que i*i es
    # impar, impar+impar es par y esos ya los descart� antes
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
    if N == 2:
        return [2]
    primes = [2]
    for i in range(3,N):
        isprime = True
        for j in primes:
            if i%j==0:
                isprime = False
                break
        if isprime == True:
            primes.append(i)
    return primes



if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='parser.')
    parser.add_argument('number',type=int)
    parser.add_argument('method')
    parsed_args = parser.parse_args()
    N = parsed_args.number
    M = parsed_args.method
    # TODO hacer esto mejor con los m�todos de argparse
    if not M == "E" and not M == "F":
        print("Bad Method")
        quit()
    main(N,M)
