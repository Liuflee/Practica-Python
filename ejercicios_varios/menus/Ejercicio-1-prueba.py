""""Se desea evaluar que red social están usando con más frecuencia los jóvenes Instagram o TikTok,
 para esto se tomó una muestra 
de 50 jóvenes entre 12 y 18 años. 
Se les preguntará que red social prefieren, su edad y si tienen pareja o no. Desarrolle un algoritmo que permita saber:

Red social más utilizada

Promedio de edad de usuarios de Instagram y TikTok
Cuantos jóvenes que usan Instagram están en solteros.
Deberá crear un algoritmo en pseudocódigo que de solución a este problema."""

contador_tiktok = 0
contador_instagram = 0
edad_ig = 0
edad_tt = 0
contadorEstadoIG = 0
contador_edad = 0
lista_estado = ("no", "n")
red_lista = ("instagram", "tiktok", "ig", "tt")

while contador_edad < 50:

    edad = int(input("¿Cual es su edad?: \n"))

    if 11 < edad < 19:

        contador_edad += 1
        red_social = input("\n¿Instagram o Tiktok?: \n").lower()
        estado_civil = input("'\n¿Tienes pareja? (Si) o (No): \n").lower()

        if red_social not in red_lista:
            print("\nOpcion no valida\n")
        else:
            if red_social == red_lista[0]:
                contador_instagram += 1
                edad_ig += edad
                if estado_civil in lista_estado:
                    contadorEstadoIG += 1
            else:
                contador_tiktok += 1
                edad_tt += edad
    else:
        print("\nEdad no valida\n")

promedioIG = round((edad_ig / contador_instagram), 1)
promedioTT = round((edad_tt / contador_tiktok), 1)

if contador_instagram == contador_tiktok:
    print("\nAmbas redes sociales son usadas por igual\n")
elif contador_tiktok < contador_instagram:
    print("\nLa red social mas utilizada es Instagram\n")
else:
    print("\nLa red social mas utilizada es TikTok\n")

print(f"El promedio de usuarios que usan Instagram es: {promedioIG}\n")
print(f"El promedio de usuarios que usan TikTok es: {promedioTT}\n")
print(f"La cantidad de usuarios que usan Instagram y estan solteros es: {contadorEstadoIG}\n")
