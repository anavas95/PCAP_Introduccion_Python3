#Fundacion Kinal
#Centro educativo tecnico laboral Kinal
#Perito en electronica
#cuarto grado.
#Taller de electronica analogica
#Alumno: Luis Alejandro Lopez Navas
#Carnet: -------------
#Actividad: Tipo de dato Listas

#Una lista en python es una coleccion de datos, agrupados bajo un mismo nombre
#similar al tipo de dato struc en ANSI C. Este tipo de dato como tal nos permite
#tener varios tipos de datos bajo el mismo 'alias'

#Para declarar las listas se realiza de la siguiente manera

_myList = [] #Esto es una lista vacia, es decir no tiene ningun tipo de dato almacenado dentro.

#Que ventajas tiene usar una lista vacia? Pues tiene la ventaja de ser mutable
#es decir nostros podemos modificar los elementos que contiene. 

#Por ejemplo esto es una lista.

_numberList = [1,2,3,4,5]
print('Esto es una lista que contiene unicamente numeros ', _numberList)


#Este es otro ejemplo de como  es una lista

_charList = ['Colegio', 'Carrera', 'Grado', 'Seccion', 'Curso' , 'Nombre', 'Carnet']
print('Esto es una lista que contiene unicamente strings ', _charList)

#Esto es otro ejemplo de como es una lista con varios tipos de datos
_difList = ['Luis', 'Alejandro', 91, 13, True]
print('Esto es una lista que contiene varios tipos de datos ', _difList) 
