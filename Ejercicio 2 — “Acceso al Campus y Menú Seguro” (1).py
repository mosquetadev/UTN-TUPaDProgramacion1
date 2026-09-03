#1el usuario ingresa con datos correctos
usuario_logueado= False
intentos=0
clave_valida="python123"
usuario = "alumno"
 #intento de ingreso al campus 
while usuario_logueado==False: 
  usuario_ingresado= input("Ingrese su usuario")
  clave1= input("Ingrese su clave")
  intentos+=1 #los intentos fallidos se van sumando
  if usuario_ingresado== usuario and clave1== clave_valida:
    # se corta el bucle al ingresar datos correctos
    print(f"Intentos {intentos}/3 - Usuario: {usuario}" )
    print(f"Clave: {clave_valida}")
    print("Acceso concedido.")
    usuario_logueado=True
  elif intentos==3: #aca se llega al maximo de intentos
    print("Cuenta bloqueada")            
    break
  else:
    print(f"Intentos {intentos}/3 - Usuario: {usuario}" )
    print(f"Clave: {clave_valida}")
    print("Error: Credenciales invalidas")



#Ingreso al menu interactivo
print("===== MENU =====")
while usuario_logueado==True:
  opcion_menu= input("Elija la opción deseada: \n1- Ver estado inscripción \n2- cambiar clave \n3- Mostrar mensaje motivacional \n4- Salir ")
  #Validar que sea numero y este e/1 y 4

  if opcion_menu.isdigit():
    opcion_menu=int(opcion_menu)
    if 5>opcion_menu>0:
      if opcion_menu==4:
        break
      elif opcion_menu==3 :
        print("Al mal tiempo, buenas mosquetas 🐷")
      elif opcion_menu==1:
        print("Inscripto")
      elif opcion_menu==2:
        clave2= input("Ingrese su nueva clave minimo 6 caracteres") 
        
        if len(clave2)>=6:
          confirmar2= input("Confirme su nueva clave")
          if clave2 ==confirmar2:
            clave_valida= clave2
            print("Nueva clave confirmada!")
          else:
            print("Error: Las claves no coinciden")
        else:
          print("Error: Las clave debe tener 6 digitos o más")
    else:
      print("Error: Ingrese un numero valido entre 1 y 4")
  else:
    print("Error: Ingrese un caracter numerico")





