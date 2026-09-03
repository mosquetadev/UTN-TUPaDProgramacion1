#Stats gladiador
gladiador = ''
hp_gladiador = 100
pociones_vida = 3
dmg_gladiador = 15

#Stats enemigo
hp_enemigo = 100
dmg_enemigo = 12

turno_gladiador= True
esta_jugando = True

gladiador = input("Ingresa el nombre del ⚔ GLADIADOR ⚔")
while not gladiador.isalpha():
    print("Error: Ingresa un nombre valido, sin numeros")
    gladiador = input("Ingresa el nombre del gladiador")

while hp_gladiador > 0 and hp_enemigo > 0:

    print()
    print("====MENU GLADIADOR====")
    print(f"Vida: {hp_gladiador}❤")
    print(f"Pociones: {pociones_vida}🍼")
    print()
    print("1.⚔ Ataque pesado ")
    print("2.🌪 Rafaga veloz ")
    print("3.⛑ Curar ")
    print("====MENU GLADIADOR====")
    print()
  

    opcion = input("Ingresa tu siguiente acción: ")
    while not opcion.isdigit() or not (1 <= int(opcion) <= 3):
        print("Error: Debes ingresar una opcion valida (1, 2 o 3).")
        opcion = input("Elije una opcion: ")
    opcion = int(opcion)


    #1 ATAQUE PESADO
    if opcion == 1:
        if hp_enemigo < 20:
            hp_enemigo -= dmg_gladiador * 1.5
            print(f"DAÑO CRITICO 💫💥🕷 {dmg_gladiador * 1.5}pts")
        else:
            hp_enemigo -= dmg_gladiador
            print(f"Atacaste al enemigo 🕷 por {dmg_gladiador}pts! ES MUY EFECTIVO ")

    #2 RAFAGA VELOZ
    if opcion == 2:
        for ataque in range(3):
            hp_enemigo -=5
            print("Golpe conectado! 5 de daño 🌪")
    
    #3 CURAR
    if opcion == 3:
        if pociones_vida == 0 :
            print("Te quedaste sin pociones, podes comprar más en Temu por 0.99$")
        else:
            print("+30 de vida ♥")
            hp_gladiador += 30
            pociones_vida -=1


    turno_gladiador = False
    if hp_enemigo >0:
        hp_gladiador -= dmg_enemigo
        print()
        print("-----TURNO ENEMIGO-----")
        print(f"Vida = {hp_enemigo}🕷")
        print("El enemigo te ataco por 12Pts de daño, No es muy efectivo") 
        print("-----------------------")

    if hp_enemigo <= 0:
        print(f"VICTORIA,{gladiador} mataste al aracnido 🕷")
        esta_jugando = False
    elif hp_gladiador <=0:
        print(f"DERROTA,{gladiador} has caido ante Aragog 🕷")
        esta_jugando = False
        
        
    










    