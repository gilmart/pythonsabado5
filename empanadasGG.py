print("***MENU***")
print("1. Agregar 1 empanada")
print("2. Mostrar empanada")
print("3. SALIR")
opcion=100
#Datos Empanada
#Sabor
#Ingredientes
#Precio Fabricacion
#Precio Venta
suma=1
empanadas=[]

while(opcion != 3):
    empanada={}
    opcion= int(input(f'Digite una opcion: '))
    if(opcion == 1):
        empanada['sabor']=input(f'Digite el sabor de la empanada: ')
        for suma in range(3):
            empanada['ingredientes']=input(f'Digite el ingrediente {suma} de la empanada: ')
            suma +=1
        empanada['precioF']=input(f'Digite el costo de fabrica: ')
        empanada['precioV']=input(f'Digite el costo de venta: ')
        empanadas.append(empanada)
    elif(opcion == 2):
       print(empanadas)
       print('funcionando')
for llave,valor in empanada.items():
            print(llave)
            print(valor)