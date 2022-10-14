def bin_exp_mod(a, n, b): # => O(n), la funcion vendria siendo lineal
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
        return 1

    if n % 2 == 1: # O(n)
        # si n es impar entrara en este if volviendo a ejecutar la funcion con n - 1
        # print('i = ',(bin_exp_mod(a, n-1, b) * a) % b)
        return(bin_exp_mod(a, n-1, b) * a) % b
        # al ejecutar este funcion si n es mayor que 1 entrara a ejecutar la funcion hasta llegar a r y asi sucesibamente hasta que n sea igual a 0

    # si n es par volvemos a ejecutar la funcion dividiendo n / 2
    r = bin_exp_mod(a, n / 2, b) # O(1)
    # print('r = ',r)
    # la ejecucion de esta funcion entrara convertira a n en 1 haciendo que entre en el segundo if
    return (r * r) % b

# print(bin_exp_mod(3,4,5))
# print(bin_exp_mod(7,13,10))
# En este caso me mareé con la ejecucion de funciones dentro de la misma funcion y no pude refactorizar

from collections.abc import Sequence

def decimal_to_binary(no_of_variable: int, minterms: Sequence[float]) -> list[str]: # => O(n**2), la funcion vendria siendo cuadratica
    """
    >>> decimal_to_binary(3,[1.5])
    ['0.00.01.5']
    """
    temp = [] # O(1)
    for minterm in minterms: # O(n)
        string = "" # O(1)
        for i in range(no_of_variable): # O(n)
            string = str(minterm % 2) + string # O(1)
            print(string)
            minterm //= 2
        temp.append(string) # O(1)
    return temp

# O(1) + O(n) * O(1) + O(n) * O(1) + O(1) => O(n) * O(n) * O(1) => O(n**2)

print(decimal_to_binary(3,[1.5]))
# En este caso me parece que el codigo ya esta optimizado y no siento que sea necesario refactorizarlo