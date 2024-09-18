x = 5
y = "John"
print(x)
print(y)

z = 4
z = "Sally"
print(z)

#Esta es la forma que utilizamos para definir variables en phyton
#Formas erroneas de definir 2myvar = "John", my-var = "John", my var = "John"

#Asigancion de muchos valores a multiples variables
x1, y1, z1, = "orange", "Banana", "Cherry"
print(x1)
print(y1)
print(z1)

#Un valor a multiples variables 
x3 = y3 = z3 = "Greaps"
print(x3)
print(y3)
print(z3)

#Desempaquetar una coleecion
#Si tiene una coleccion de valores phyton le permite extraer los 
#Valores en variables, esto se llama desempacado
fruits = ["apple", "pear", "peach"]
x4, y4, z4 = fruits
print(x4)
print(y4)
print(z4)

#La forma de imprimir varias variables dentro 
#del mismo print es separandolas por comas o el signo operador "+"
#Nota: al combinar una cadena y un numero con el operador + nos lanzara un error
#La forma correcta de unirlas es con la coma 
#Nota: para los numeros el + funciona como operador

x6 = 18
y6 = "Juan"
z6 = 20
print(x6, y6)
print(x6 + z6)

#Aunque se puden utilizar ambas es mas facil y eficaz 
#la coma ya que con esta podemos unir multivariables
