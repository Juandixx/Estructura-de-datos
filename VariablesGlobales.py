#esta es la forma de definir las variables globales 
x = "Awesome"
#Las variables globales pueden ser utilizadas por todos, tanto dentro de funciones y exterior.

def Funcion():
    #Creamos una funcion y usamos la variable dentro de la funcion de esta manera 
    print("phyton is ", x)
Funcion()

def Funcionx():
    #tambien podemos crear una variable dentro de la funcion con el mismo nombre de la variable global
    x = "Fantastic"
    print("Phyton is ", x)
Funcionx()


def Funciony():
    #tambien podemos crear una variable global con la palara clave "global"
    global x
    x = "Fantastic"
Funciony()

print("Phyton is ", x)