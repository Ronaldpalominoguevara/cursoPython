## Se inicializar variable que será el contador, solo pasa por aquí al iniciar el ciclo var a =0;
# num = [1,2,3,4,5,6,7,8,9]
# print('x^2 loop:')
# for x in num:
#     y = x * x
#     print(str(x) + '*' + str(x) + '=' + str(y))


## while tambien es una estructura de ciclo
## imt es un metodo de python que transforma un dato
## tipo texto a un dato de tipo numerico real o entero
## input es un metodo de python que pide un dato 
## por consola al usuario 
# condicion= True
# while condicion==True:
#     numero=int (input("ingrese el numero ganador:"))
#     if numero ==10:
#         print("ganaste el premio")
#         condicion=False
#     else:
#         print("sientate chato ese no es el numero")

## crear un programa que me pida mi edad 
## si ingreso una edad incorrecta el programa
## seguira pidiendo mi edad 
## si es la edad correcta me mostraba un mensaje  
## y se termina la ejecucion

condiciones== True
while condiciones== True:
    numero=int(input("ingrese un numero"))
    if numero==20:
        print("correcto")
        condiciones=False
    else:
        print("incorrecto")

password="77233270"
condicion=True
intesntos=1
while condicion==True:
    print("este es tu",intentos,"intentos")
    newPassword=input("ingresa el password correcto:")
    ifnewPassword==password:
        print("bienvenido al sistema joven")
        condicion=False
    else:
        print("eres un gil")
        intentos+=1

##ejercicios de ejemplos 1
contador=0
while contador<5:
    print("hola",contador)
    contador+=1


## ejercicios de ejemplos 2
for numero in range(1,11):
    print(numero)


## ejercicios 3
condicion=True
eval=1
while condicion==True
   if eval==5:
    print("estamos en 5")
    condicion=False
   else:
    eval+=1