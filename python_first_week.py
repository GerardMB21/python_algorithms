# x = True constante => O(1), una asignacion siempre es constante

# for i in range(0, len(dataList), 2) logaritmico => O(log n), un recorrido por saltos o divisiones siempre es logaritmico

# for i in dataList  lineal => O(n), los bucles de recorrido por cada item siempre son lineales

# def merge_sort(data):
#    ... merge_sort(rigth), merge_sort(left) lineal logaritmico => O(n log n), la llamada de la misma funcion dentro de esa funcion siempre es lineal logaritmico

# def buble_sort(data):
#   ... if i in range(len(data) - 1) cuadratica => O(n2), el reordenamiento constante de una lista hara que se ejecute en funcion cuadratica de la cantidad de datos que contiene por ende siempre sera cuadratica

# def cubic_sort(data):
#   for i in data:
#       for j in data:
#           for k in data:
#               print(x,y,z) cubica => O(n3), la iteracion contante de for en bucle iterar la lista en funcion de la cantidad de de iteraciones de for por lo tanto sera n elevado a la m

def bin_exp_mod(a, n, b):
    """
    >>> bin_ex_mod(3, 4, 5)
    1
    >>> bin_exp_mod(7, 13, 10)
    7
    """
    # mod b
    assert not (b == 0), "This cannot accept modulo that is 0"
    if n == 0: # O(n)
        # si el segundo argumento n es 0 returna 0
        # print('first if',n)
        print('return first if')
        return 1

    if n % 2 == 1: # O(n)
        # si n es impar entrara en este if volviendo a ejecutar la funcion con n - 1
        # print('second if',n)
        # print('return second if',(bin_exp_mod(a, n-1, b) * a) % b)
        print('return second if')
        return(bin_exp_mod(a, n-1, b) * a) % b
        # al ejecutar este funcion si n es mayor que 1 entrara a ejecutar la funcion hasta llegar a r y asi sucesibamente hasta que n sea igual a 0

    # si n es par volvemos a ejecutar la funcion dividiendo n / 2
    r = bin_exp_mod(a, n / 2, b) # O(1)
    # print('r = ',r)
    # la ejecucion de esta funcion entrara convertira a n en 1 haciendo que entre en el segundo if
    # print('ultimo return',(r * r) % b)
    print('ultimo return')
    return (r * r) % b

bin_exp_mod(3, 4, 5) # => O(n) + O(n) + O(1) = O(n)
print(bin_exp_mod(7, 13, 10))

# def proob():
#     return(1*3)%5

# print(proob())