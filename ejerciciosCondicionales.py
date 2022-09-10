'''
edad=int(input('Ingrese la edad: '))
    
if(edad <18):
    print('usted es menor de edad')
else:
    print('usted es mayor de edad')
   

password=(input('Ingrese password: ')).casefold()
password2=(input(f'Ingrese password nuevamente: ')).casefold()

if(password==password2):
    print(f'password correcta: {password}')
else:
    print(f'password incorrecta {password2} intente nuevamente') 
num1=int(input('Ingrese numero1: '))
num2=int(input('Ingrese numero2: '))

while(num2==0):
    num2=int(input('Ingrese numero2 nuevamente: '))
    if(num2 != 0):
        resultado=num1/num2
        print(resultado)


diccionario={'Euro':"€", 'Yen':"¥", 'Dolar':"$"}

usuario =input('Ingrese divisa: ')
if usuario.title() in diccionario:
    print(diccionario[usuario.title()])
  
else:
    print(f'no se encontró divisa {usuario}')


monedas = {'Euro':'€', 'Dollar':'$','Yen':'¥'}
moneda = input("Introduce una divisa: ")
if moneda.title() in monedas:
    print(monedas[moneda.title()])
else:
    print("La divisa no está.")
    '''
'''

usuario={}
usuario['nombre']=input('ingrese nombre: ')
usuario['edad']=input('ingrese edad: ')
usuario['direccion']=input('ingrese direccion: ')
usuario['telefono']=input('ingrese telefono: ')

print(usuario)
print(usuario['nombre'] +' tiene ' + usuario['edad'] + ', vive en ' + usuario['direccion'] +' y su telefono es: ' + usuario['telefono'])

print('1. agregar usuario')
print('2. enseñar usuario')

usuarios=[]
opcion=100

while(opcion!=0):
    usuario={}
    opcion=int(input('ingrese una opcion: '))

    if opcion == 1:
        usuario['nombre']=input('ingrese nombre: ')
        usuario['edad']=input('ingrese edad: ')
        usuario['direccion']=input('ingrese direccion: ')
        usuario['telefono']=int(input('ingrese telefono: '))

        usuarios.append(usuario)
    elif(opcion==2):
        usuario={}
        for llave,valor in usuario.items():
            print(llave)
            print(valor)


print('1. agregar usuario')
print('2. enseñar usuario')

usuarios=[]
opcion=100

while(opcion!=0):
    usuario={}
    opcion=int(input('ingrese una opcion: '))

    if opcion == 1:
        nombre=input('ingrese nombre: ')
        edad=input('ingrese edad: ')
        direccion=input('ingrese direccion: ')
        telefono=int(input('ingrese telefono: '))

        usuario={'nombre':nombre, 'edad':edad}

        usuarios.append(usuario)
    elif(opcion==2):
        usuario={}
        for llave,valor in usuario.items():
            print(llave)
            print(valor)

frutas={
    'platano': 1.35,
    'manzana':0.80,
    'pera':0.85,
    'naranja':0.75
}

fruta=input(f'digite una fruta: ')
kilos=int(input(f'digite los kilos: '))

if fruta in frutas:
        valorKilos=kilos * frutas[fruta]
        print(valorKilos)

'''
dia=int(input('dd: '))
mes=int(input('mm: '))
year=int(input('aaaa: '))

fecha={'dia': dia, 'mes':mes, 'year':year}

meses={
    'enero':1,
    'febrero':2,
    'marzo':3
}

print(f'${dia} de mes ${meses[mes]} de year ${year}')

print