estacion = int(input(f'por favor, introduce un número de mes: '))

if 0<estacion<3 or 11<estacion<13:
    print(f"el mes: {estacion} esta en la estación: Invierno")
elif 3<estacion<6:
    print(f"el mes: {estacion} esta en la estación: Primavera")
elif 6<estacion<10:
    print(f"el mes: {estacion} esta en la estación: Verano")
elif 9<estacion<11:
    print(f"el mes: {estacion} esta en la estación: Otoño")
else:
    print(f"el número del mes introducido no es correcto")