# program.py
sum = 1 + 2
print(sum)

print("\n") #Imprimir un espacio vació para separar los mensajes

# Impresión en pantalla print('Hola desde la consola')
print('Hola desde la consola')

print("\n")

# Tu turno, prueba el fragmento de código anterior
sum = 1 + 2 #3
product = sum * 2
print(product)

print("\n")

# Declaramos la variable
distancia_a_alfa_centauri = 4.367

# Descubrimos su tipo de dato
print(type(distancia_a_alfa_centauri))

print("\n")

#Manejar Fechas
#Importamos la biblioteca
from datetime import date

#Obtenemos la fecha actual
date.today()

#Mostrar la fecha en la consola
print(date.today())

print("\n")

#Concatenar string con la fecha}
#Ejemplo de error
#print("Today's date is: " + date.today())

# Tu turno ejecuta el siguiente comando: print("Today's date is: " + str(date.today()))
print("Today's date is: " + str(date.today().strftime("%d/%m/%Y")))