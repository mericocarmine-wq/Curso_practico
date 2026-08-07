#1 esto es una funcion que devuelve el doble de un numero
def numero_doble(numero):
    return numero * 2   
print(numero_doble(5))

#2 esto es una función que calcula el precio total de dos productos
def calcular_precio_total(precio1, precio2):
    return (precio1 + precio2)
print(calcular_precio_total(20.50, 10.00))


#3 esta es una función que calcula el descuento de un producto
def calcular_descuento(precio):
       if precio >= 100:
        return (precio * 0.90)
       else:
        return (precio)
print(calcular_descuento(150))

#4 esta es una funcion que calcula aprobado, suspenso o notable de un alumno
def calificacion_alumno(nota):
    if nota >= 9:
        return "Sobresaliente"
    elif nota >= 7:
        return "Notable"
    elif nota >= 5:
        return "Aprobado"
    else:
        return "Suspenso"
print(calificacion_alumno(8))

#5 esta es una funcion que calcula mayoria de edad o menor de edad
def es_mayor_de_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"
print(es_mayor_de_edad(20))

def natascha_pago_alquiler(habitacion1, habitacion2):
    return habitacion1 + habitacion2
print(natascha_pago_alquiler(1000, 1500))