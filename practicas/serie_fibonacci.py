#Números Fibonacci
#Desarrolla un programa el cual nos permita conocer los primeros n números de la serie Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, #89, 144, …

"""
Definir una función llamada fibonacci.
La función debe poseer como parámetro la variable _maxnumber.
La función debe recibir como argumento un número entero mayor a 0.
La función debe retornar, mediante una lista, los primero n números (con respecto al parámetro) del a serie Fibonacci.
"""

def fibonacci(_maxnumber):
    resultado = [0, 1]
    num = 0 + 1

    # Validaciones
    if _maxnumber is None: 
        print("El parámetro {} es incorrecto, el parámetro debe contener un valor".format(_maxnumber))	
        return []
    if _maxnumber == "":
        print("El parámetro {} es incorrecto, el parámetro debe contener un valor entero".format(_maxnumber))	
        return []        
    if not (str(_maxnumber)).isdigit():
        print("El parámetro {} es incorrecto, debe ser un entero".format(_maxnumber))
        return []
    elif int(_maxnumber) <= 0:
        print("El parámetro {} debe ser un entero mayor a 0".format(_maxnumber))
        return []

    # Generar la serie
    for i in range(int(_maxnumber)):
        num += resultado[i]
        resultado.append(num)

    return resultado[:int(_maxnumber)]

numero = input("Introduzca el número para generar la serie de Fibonacci: ")
lst_resultado = fibonacci(numero)

print(lst_resultado)
