'''
diccionario ={
'nombre':"juan",
'edad':33,
'hincha': True,
'comida': ['pizza', 'pollo','alpiste'],
}

print(diccionario['nombre'])
'''
diccionario ={}

diccionario['nombre']=input("digite el nombre: ")
print(diccionario)
print(diccionario['nombre'])

for llave,valor in diccionario.items():
    print(llave)
    print(valor)