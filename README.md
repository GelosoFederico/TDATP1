# TDATP1
## TP1 de TDA
## Link overleaf: https://v2.overleaf.com/7789198523cszqhrmdkvyp

### Parte 1: Variante de Gale Shapley

En la ciudad de Buenos Aires se llevarán a cabo N recitales en diferentes barrios. Se ha realizado una convocatoria a bandas de música del underground. Como resultado, se han presentado M bandas.

Cada banda tiene diferentes preferencias sobre en cual recital tocar. Asimismo cada comité organizador del recital tiene un listado de preferencias de bandas. Los organizadores se comunican con las bandas para ofrecerles participar y pueden contratar como mucho a X bandas distintas. De la misma manera, una banda puede participar en como mucho Y recitales.

Se solicita:

Utilizar una variante de Gale-Shapley para resolver el problema. Explicarlo y presentar el pseudocódigo.

Analizar y justificar la complejidad del algoritmo

Analice las condiciones para que el algoritmo propuesto retorna un matching estable y/o perfecto.

Suponga que los organizadores pueden tener preferencias similares sobre diferentes bandas y visceversa. ¿Cómo afecta esto en el algoritmo? ¿Considere que en caso de empate el involucrado decida desempatar tirando una moneda. ¿Cómo se ve afectado el proceso?

Programe la solución propuesta en el punto 1. Genere archivos random y ejecute el programa para los siguientes valores de N, M, X e Y. 

¿Qué ocurre en cada caso?:

N = 10, M = 10, X = 1, Y = 1

N = 10, M = 5, X = 2, Y = 2

N = 10, M = 5, X = 2, Y = 1

Compare la complejidad teórica con la del algoritmo programado.

Información adicional:

Cada recital contará con un archivo llamado “recital_[nro]”. en cada línea estarán en forma ordenada decreciente sus preferencias de bandas.

Cada banda contará con un archivo llamado “banda_[nro]”. En cada línea estarán en forma ordenada decreciente sus preferencias de recitales.

Las bandas estarán identificadas por números entre el 1 y el M.

Los recitales estarán identificados por números entre el 1 y el N.

Al programa se le deben pasar por parametro de inicio los valores numéricos enteros en el siguiente orden: N M X Y


### Parte 2: Complejidad algorítmica

Eratóstenes de Cirene, matemático, astrónomo y geógrafo griego propuso un algoritmo para calcular los números primos menores a un valor “N”.

Iniciaba escribiendo todos los numeros de 1 a N. Luego en forma creciente partiendo desde el 2, iba tomando los números y tachando a sus múltiplos (menores o iguales a n). Al repetir el procedimiento el primer valor no tachado corresponde a un número primo. Se conoce a este procedimiento como “criba de Eratóstenes”.

Describa en pseudocódigo el algoritmo (procure realizar la solución más eficiente posible. Investigue!)

Analice y justifique su complejidad.

Describa en pseudocódigo el algoritmo de fuerza bruta para calcular los números primos y analice y justifique su complejidad.

Programe ambas soluciones (punto 1 y 3).

Grafique los tiempos de ejecución de ambos algoritmos para los siguientes valores de N: 100, 1.000, 10.000, 100.000, 1.000.000, 10.000.000

Analice los resultados obtenidos en base a la complejidad teórica de los mismos.

Información adicional:

El algoritmo debe recibir por parámetro:

número “N”.

F (fuerza bruta) o E (Erastóstenes)

Debe devolver:

Lista de los números primos desde 2 hasta “N”.

Tiempo total de ejecución
