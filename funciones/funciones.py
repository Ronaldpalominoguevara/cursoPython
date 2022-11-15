 ##una función como un conjunto de líneas de código que realizan una tarea específica y pueden tomar “Argumentos” para diferentes “Parámetros” 
 ##que modifiquen su funcionamiento y los datos de salida.Una función te permite 
 ##implementar operaciones que son habitualmente utilizadas en un programa y, de esta manera, reducir la cantidad de código.
 ## 2 tipos de funciones
 ## funciones propias de python
#  print()##sirve para mostrar mensaje o resultado
#  int()##esta funcion sirve para convertir string en entero
#  input()##esta funcion sirve para pedir datos al usuario
 ##todo lo que se ingrese en input sera tomado como texto 

 ## funciones creadas
 ## creando funcion  
#  def suma(a,b):
#     resultado=a+b
#     return resultado
# ## uso de funcion 
# print(suma(4,6))
 
# numero = int(input("Dígame cuántas palabras tiene la lista: "))

# if numero < 1:
#     print("¡Imposible!")
# else:
#     lista = []
#     for i in range(numero):
#         print("Dígame la palabra", str(i + 1) + ": ", end="")
#         palabra = input()
#         lista += [palabra]
#      print("La lista creada es:", lista)



## ejercicios de tabla de multiplicacion 
# for numeros in range(1,11):
#     print(numeros,"*",2,"=",numeros*2)

##ejercicios de la tabla de multiplicacion 
# numero=int(input("ingrese el numero de la tabla desea mostrar:"))
# for numeros in range(1,11):
#     print(numeros,"*",numero,"=",numeros*numero)


# numero="10"
# int(numero)
## int es el nombre de la funcion () y dentro de 
# parentesis van los parametros
# sentence=input("ingrese una oracion:")
# def countVocals(texto):
#   vocales=["a","e","i","o","u"]
#   contadorVocales=0
#   for letras in texto:
#    if letras in vocales:
#       contadorVocales+=1
#   return contadorVocales
# print("la cantidad de vocales es:",countVocals("sentence"))


##operadorMatematico(numeroUno ,numeroDos,operacion)
##operadorMatematico(4,5,"suma")
##por consila la suma de 4+5

# def mensaje(nombre,apellido,accion):
#   if accion == "saludo":
#     mensaje="hola",nombre,apellido,"como estas"
#   elif accion == "despedida":
#     mensaje="adios",nombre,apellido
#   return mensaje
  
# respuesta=mensaje("ronald","guevara","despedida")
# print(respuesta)

# ##crear una funcion de operaciones matematicas 
# def operaciones(numero1,numero2,operacion):
#   if operacion=="suma":
#     operaciones="la suma de:" ,numero1, "+" ,numero2, "es" ,numero1+numero2
#   elif operacion=="resta":
#     operaciones="la resta de:" ,numero1, "-" ,numero2, "es" ,numero1-numero2
#   return operaciones
# print(operaciones(10,2,"resta"))

##vocales convertido en funciones

# sentence=input("enter sentence:")
# vocales=["a","e","i","o","u"]
# def countVocal(oracion,vocal):
#   contador=0

#   for word in oracion:
#     if word in vocal:
#       contador+=1
#   return contador
# print(countVocal(sentence,vocales))



