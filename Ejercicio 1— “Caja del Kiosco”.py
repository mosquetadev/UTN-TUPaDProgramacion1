nombre_valido= False
while nombre_valido ==False:
  nombre_cliente = input("Ingrese el nombre del cliente")
  #cantidad_prod= int(input("Ingrese cantidad de productos"))
  if  nombre_cliente.isalpha() and nombre_cliente.strip() != "":
    nombre_valido=True
  else:  
    print("Error: Sólo texto y no puede estar vacio")

prod_valido= False
while prod_valido ==False:
  cant_prod = input("Ingrese cantidad de productos")
  #aca valido si es numero
  if  cant_prod.isdigit() :
    cant_prod=int(cant_prod)
    if cant_prod >0:
      prod_valido=True
    else:
      print("Error:Ingrese un numero mayor a 0")
  else:  
    print("Error: Debe ser un caracter numerico")

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cant_prod}")

total_precio= 0
descuentos_acumulados= 0
for producto in range(cant_prod):

  #VALIDAR PRECIO INGRESADO
  precio_valid= False
  while precio_valid==False:
    precio = input(f"Ingrese precio del producto {producto+1}")
  #valido si es numero
    if precio.isdigit():
      precio=int(precio)
      total_precio= total_precio + precio
      precio_valid= True
    else:  
      print("Error: Debe ser un caracter numerico")

  #VALIDAR SI TIENE DESCUENTO
  desc_valid= False
  while desc_valid==False:
    hay_descuento= input(f"¿El producto {producto+1} tiene descuento? \n S (si) N (no)")
 #validar s o n SIN case_sensitive
    if hay_descuento.lower() in ("s","n"):
      desc_valid= True
    else:
      print("sólo s ó n")
  print(f"Producto {producto +1} - Precio: ${precio} Descuento (S/N): {hay_descuento}") 
  if hay_descuento.lower() =="s":
    descuentos_acumulados+= precio *10/100 
  promedio_prod= (total_precio-descuentos_acumulados)/cant_prod
  total_desc=total_precio-descuentos_acumulados
print(f"Total sin descuentos: ${total_precio}")  
print(f"Total con descuentos: ${total_desc:.2f}") 
print(f"Ahorro: ${descuentos_acumulados:.2f}")
print(f"Promedio por producto: ${promedio_prod:.2f}")


    
  






  