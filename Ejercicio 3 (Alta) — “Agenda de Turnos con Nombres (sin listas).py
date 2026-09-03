menu_active = True

lunes1 = ''
lunes2 = ''
lunes3 = ''
lunes4 = ''

martes1 = ''
martes2 = ''
martes3 = ''

operador = input("Nombre del operador: ")
while not operador.isalpha():
    print("Error: El nombre solo puede contener letras.")
    operador = input("Nombre del operador: ")

while menu_active == True:

    option = input("============MENU============ \n1. Reservar turno \n2. Cancelar turno (por nombre) \n3. Ver agenda del día \n4. Ver resumen general \n5. Cerrar sistema \n============================")

    if option.isdigit():
        option = int(option)
        if 1 <= option <= 5:
            # RESERVAR TURNO
            if option == 1:
                nombre = input("Ingresa el nombre de la persona que tendrá la reserva: ")

                while not nombre.isalpha():
                    print("Error: El nombre solo puede contener letras.")
                    nombre = input("Ingresa el nombre de la persona que tendrá la reserva: ")

                dia = input("Que día querés reservar? 1: Lunes 2: Martes: ")

                if dia.isdigit():
                    dia = int(dia)
                    if dia == 1 or dia == 2:
                        if dia == 1:
                            if nombre == lunes1 or nombre == lunes2 or nombre == lunes3 or nombre == lunes4:
                                print("Ya tenes un turno para el día Lunes")
                            elif lunes1 == '':
                                lunes1 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día LUNES!")
                            elif lunes2 == '':
                                lunes2 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día LUNES!")
                            elif lunes3 == '':
                                lunes3 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día LUNES!")
                            elif lunes4 == '':
                                lunes4 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día LUNES!")
                            else:
                                print("No hay turnos disponibles para el día Lunes")

                        if dia == 2:
                            if nombre == martes1 or nombre == martes2 or nombre == martes3:
                                print("Ya tenes un turno para el día Martes")
                            elif martes1 == '':
                                martes1 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día MARTES!")
                            elif martes2 == '':
                                martes2 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día MARTES!")
                            elif martes3 == '':
                                martes3 = nombre
                                print("✅ Tu turno se reservó de forma correcta para el día MARTES!")
                            else:
                                print("No hay turnos disponibles para el día Martes")
                    else:
                        print("Error: Ingresa una opción 1:Lunes 2:Martes")
                else:
                    print("Error: Debes ingresar 1 o 2")

            # CANCELAR TURNO POR NOMBRE
            if option == 2:
                dia = input("Que día querés cancelar? 1: Lunes 2: Martes: ")

                if dia.isdigit():
                    dia = int(dia)
                    if dia == 1 or dia == 2:
                        nombre = input("Ingresa el nombre de la persona que cancelará la reserva: ")

                        while not nombre.isalpha():
                            print("Error: El nombre solo puede contener letras.")
                            nombre = input("Ingresa el nombre de la persona que cancelará la reserva: ")

                        if dia == 1:
                            if lunes1 == nombre:
                                lunes1 = ""
                                print("✅ Turno eliminado correctamente")
                            elif lunes2 == nombre:
                                lunes2 = ""
                                print("✅ Turno eliminado correctamente")
                            elif lunes3 == nombre:
                                lunes3 = ""
                                print("✅ Turno eliminado correctamente")
                            elif lunes4 == nombre:
                                lunes4 = ""
                                print("✅ Turno eliminado correctamente")
                            else:
                                print("Error: No hay turnos asignados a tu nombre.")

                        if dia == 2:
                            if martes1 == nombre:
                                martes1 = ""
                                print("✅ Turno eliminado correctamente")
                            elif martes2 == nombre:
                                martes2 = ""
                                print("✅ Turno eliminado correctamente")
                            elif martes3 == nombre:
                                martes3 = ""
                                print("✅ Turno eliminado correctamente")
                            else:
                                print("Error: No hay turnos asignados a tu nombre.")
                    else:
                        print("Error: Ingresa una opción 1:Lunes 2:Martes")
                else:
                    print("Error: Debes ingresar 1 o 2")

            # AGENDA DEL DÍA
            if option == 3:
                dia = input("Que día querés ver? 1: Lunes 2: Martes: ")

                if dia.isdigit():
                    dia = int(dia)
                    if dia == 1:
                        print("-- AGENDA DÍA LUNES --")
                        print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                        print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                        print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                        print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
                    elif dia == 2:
                        print("-- AGENDA DÍA MARTES --")
                        print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                        print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                        print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")
                    else:
                        print("Error: Ingresa una opción 1:Lunes 2:Martes")
                else:
                    print("Error: Debes ingresar 1 o 2")

            # RESUMEN GENERAL
            if option == 4:
                lunes_ocupados = 0
                martes_ocupados = 0

                if lunes1 != "":
                    lunes_ocupados += 1
                if lunes2 != "":
                    lunes_ocupados += 1
                if lunes3 != "":
                    lunes_ocupados += 1
                if lunes4 != "":
                    lunes_ocupados += 1

                if martes1 != "":
                    martes_ocupados += 1
                if martes2 != "":
                    martes_ocupados += 1
                if martes3 != "":
                    martes_ocupados += 1

                lunes_disponibles = 4 - lunes_ocupados
                martes_disponibles = 3 - martes_ocupados

                print("-- RESUMEN GENERAL --")
                print(f"Lunes: {lunes_ocupados} ocupados, {lunes_disponibles} disponibles")
                print(f"Martes: {martes_ocupados} ocupados, {martes_disponibles} disponibles")

                if lunes_ocupados == martes_ocupados:
                    print(f"Lunes y Martes están empatados con {lunes_ocupados} turnos ocupados.")
                elif lunes_ocupados > martes_ocupados:
                    print(f"El día con más turnos ocupados es Lunes con {lunes_ocupados} reservas.")
                else:
                    print(f"El día con más turnos ocupados es Martes con {martes_ocupados} reservas.")

                print()

            # CERRAR SISTEMA
            if option == 5:
                menu_active = False
                print("Saliendo... Vuelva pronto!")
                break

        else:
            print("Error: Fuera de rango")
    else:
        print("Error: Opción inválida, ingresa un número válido")
