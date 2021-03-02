# Saber el factorial de un numero

def numero_valido(numero):
    # Validaciones
    if numero is None: 
        print("El parámetro {} es incorrecto, el parámetro debe contener un valor".format(numero))	
        return False
    if numero == "":
        print("El parámetro {} es incorrecto, el parámetro debe contener un valor entero".format(numero))	
        return False     
    if not (str(numero)).isdigit():
        print("El parámetro {} es incorrecto, debe ser un entero".format(numero))
        return False
    elif int(numero) <= 0:
        print("El parámetro {} debe ser un entero mayor a 0".format(numero))
        return False
    return True

def factorial(numero):
    resultado = 1

    for i in range(1, numero+1):
        resultado = i * resultado
    
    return resultado

num = input("Introduzca el número para calcular su factorial: ")
if numero_valido(num):
    fac = factorial(int(num))
    print("El factorial de {} es {}".format(num, fac))