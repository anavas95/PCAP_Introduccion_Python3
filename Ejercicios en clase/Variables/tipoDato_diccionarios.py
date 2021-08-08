#Fundacion Kinal
#Centro educativo tecnico laboral Kinal
#Perito en electronica
#cuarto grado.
#Taller de electronica analogica
#Alumno: Luis Alejandro Lopez Navas
#Carnet: -------------
#Actividad: Tipo de dato Diccionarios

#Los diccionarios son tipos de datos similares a las listas, 
#es decir es un tipo de estructura de datos, donde su diferencia 
#radica en la forma en la que se accede a sus elementos.

#Ahora veremos como se declara un diccionario y para esto haremos
#uso de las configuraciones de transistores.

_myDictionary = { 
	'Tipo de transistor': 'Transistor de union bipolar',
	'Estructura': 'NPN',
	'Configuracion': 'Emisor Comun',
	'Aplicacion': 'Amplificadores de corriente'
}

#si quisieramos ver que los datos que estan contenidos en esta estructura
#podriamos hacerlo de la siguienta manera
print(_myDictionary)

#De igual manera si quisiera acceder a un unico campo del diccionario, tendriamos
#que hacerlo de manera similar a como lo realizamos en las listas y las tuplas solo que
#en lugar de hacer referencia al indice numerico, hariamos referencia al nombre del campo.

print('El tiplo de transistor almacenado en mi diccionario es:', _myDictionary['Tipo de transistor'])