# enviar un saludo a python
print("Hola Python")

# con variables
miVariables = "Hola desde Python con variable"
print(miVariables)

# suma
x = 10
y = 5
z = x + y
print(z)

# declaración de variables
nombre = "Juan Perez"
telefono = 947474898595
email = "jperez@mail.com"
print(nombre)
print(telefono)
print(email)
print("el nombre es: " + nombre + " y su email es: " + email)
print("el nombre es: ", nombre, " y su email es: ", email)

# tipo
print(type(nombre))
u: str = "hola"
print(u)
print(type(u))

#pedir datos
datos= input("introduzca el nombre: ")
print(datos)
numero1=int(input("introduzca el primer numero:"))
numero2=int(input("introduzca el segundo numero: "))
resultado= numero1+numero2
print(numero1+numero2)

#califica tu día
puntuacion= int(input("califica del 1 al 10: "))
if puntuacion<=4:
print( "mal")

elif 4<= puntuacion<=7:
print("bien")

else:
print ("muy bien")