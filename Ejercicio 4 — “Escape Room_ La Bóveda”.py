codigo_parcial = ""
alarma = False
cerraduras_abiertas = 0
tiempo = 12
energia = 100
forzar_cerradura_seguidos = 0

nombre = input("Ingresa el nombre del agente: ")
while not nombre.isalpha():
    print("Error: El nombre solo puede contener letras.")
    nombre = input("Ingresa el nombre del agente: ")

juego_activo = True
bloqueo_por_alarma = False

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3 and alarma == False and juego_activo:
    print("\n==== ESTADO ====")
    print(f"Agente: {nombre}")
    print(f"Energia: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}/3")
    print(f"Codigo parcial: {codigo_parcial}")
    print(f"Alarma: {'ON' if alarma else 'OFF'}")
    print("================")

    print("\n==== MENU ACCIONES ====")
    print("1. Forzar cerradura (-20 energia, -2 tiempo)")
    print("2. Hackear panel (-10 energia, -3 tiempo)")
    print("3. Descansar (+15 energia max 100, -1 tiempo; si alarma ON: -10 energia extra)")

    opcion = input("Elije una opcion: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Error: Debes ingresar una opcion valida (1, 2 o 3).")
        opcion = input("Elije una opcion: ")
    opcion = int(opcion)

    # 1. Forzar cerradura (costo: -20 energia, -2 tiempo)
    if opcion == 1:
        forzar_cerradura_seguidos += 1
        energia -= 20
        tiempo -= 2

        if forzar_cerradura_seguidos == 3:
            print("FORZASTE 3 VECES SEGUIDAS, LA CERRADURA SE TRABO. ALARMA ACTIVADA!")
            alarma = True
        else:
            if energia < 40:
                print("Energia baja! Riesgo de alarma.")
                numero_alarma = input("Ingresa un numero del 1 al 3: ")
                while not numero_alarma.isdigit() or not (1 <= int(numero_alarma) <= 3):
                    print("Error: Debes ingresar un numero del 1 al 3.")
                    numero_alarma = input("Ingresa un numero del 1 al 3: ")
                numero_alarma = int(numero_alarma)

                if numero_alarma == 3:
                    print("ALARMA ACTIVADA! ⏱")
                    alarma = True
                else:
                    print("Te salvaste. Cerradura abierta. 🔓")
                    cerraduras_abiertas += 1
            else:
                print("Cerradura abierta. 🔓")
                cerraduras_abiertas += 1

    # 2. Hackear panel (costo: -10 energia, -3 tiempo)
    elif opcion == 2:
        print("Entrando en la matrix...")
        tiempo -= 3
        energia -= 10
        forzar_cerradura_seguidos = 0
        for pasos in range(1, 5):
            codigo_parcial += "A"
            print(f"Paso {pasos}: {codigo_parcial}")
            if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
                print("Decifraste el codigo. Cerradura abierta. 🔓")
                codigo_parcial = ""
                cerraduras_abiertas += 1

    # 3. Descansar
    elif opcion == 3:
        forzar_cerradura_seguidos = 0
        tiempo -= 1
        energia += 15
        if energia > 100:
            energia = 100
        if alarma:
            energia -= 10
        print(f"Descansaste. Energia actual: {energia}")

    # Regla de bloqueo por alarma
    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("SISTEMA BLOQUEADO POR ALARMA. PERDISTE.")
        bloqueo_por_alarma = True
        juego_activo = False

print("\n==== FIN DEL JUEGO ====")
if cerraduras_abiertas == 3:
    print(f"VICTORIA, {nombre}! Abriste las 3 cerraduras 💪🔓.")
elif bloqueo_por_alarma:
    print(f"DERROTA, {nombre}. El sistema se bloqueo por alarma 💀.")
elif energia <= 0:
    print(f"DERROTA, {nombre}. Te quedaste sin energia. 💀")
elif tiempo <= 0:
    print(f"DERROTA, {nombre}. Se te acabo el tiempo. ⌛💀")
