#N�meros Fibonacci
#Desarrolla un programa el cual nos permita conocer los primeros n n�meros de la serie Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, #89, 144, �

"""
Definir una funci�n llamada fibonacci.
La funci�n debe poseer como par�metro la variable _maxnumber.
La funci�n debe recibir como argumento un n�mero entero mayor a 0.
La funci�n debe retornar, mediante una lista, los primero n n�meros (con respecto al par�metro) del a serie Fibonacci.
"""

def fibonacci(_maxnumber):
    resultado = [0, 1]
    num = 0 + 1

    # Validaciones
    if _maxnumber is None: 
        print("El par�metro {} es incorrecto, el par�metro debe contener un valor".format(_maxnumber))	
        return []
    if _maxnumber == "":
        print("El par�metro {} es incorrecto, el par�metro debe contener un valor entero".format(_maxnumber))	
        return []        
    if not (str(_maxnumber)).isdigit():
        print("El par�metro {} es incorrecto, debe ser un entero".format(_maxnumber))
        return []
    elif int(_maxnumber) <= 0:
        print("El par�metro {} debe ser un entero mayor a 0".format(_maxnumber))
        return []

    # Generar la serie
    for i in range(int(_maxnumber)):
        num += resultado[i]
        resultado.append(num)

    return resultado[:int(_maxnumber)]

numero = input("Introduzca el n�mero para generar la serie de Fibonacci: ")
lst_resultado = fibonacci(numero)

print(lst_resultado)
