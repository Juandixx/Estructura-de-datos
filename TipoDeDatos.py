"""
Python tiene los siguientes tipos de datos incorporados de forma predeterminada, en estas categorías:

Tipo de Texto:	str
Tipos Numéricos:	int, float, complex
Tipos de Secuencia:	list, tuple, range
Tipo de Mapeo:	dict
Establecer Tipos:	set, frozenset
Tipo Booleano:	bool
Tipos Binarios:	bytes, bytearray, memoryview
Ninguno Tipo:	NoneType
"""

#Para obtener el tipo de dato de cualquier objeto utilizamos "type()"
#Ejemplo
x = 5
print(type(x))

#En Python, el tipo de datos se establece cuando se asigna un valor a una variable
y = "Hello world"
z = 20.5
w = 1j
a = ["apple", "banana", "cherry"] 
b = ("apple", "banana", "cherry")#No se pueden modificar despues de su creacion 
c = b"Hello"
d = {"name":"Juan", "age": 18}

print(type(y))
print(type(z))
print(type(w))
print(type(a))
print(type(b))
print(type(c))
print(type(d))

#Y asi definimos el tipo de dato
