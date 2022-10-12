 ##una función como un conjunto de líneas de código que realizan una tarea específica y pueden tomar “Argumentos” para diferentes “Parámetros” 
 ##que modifiquen su funcionamiento y los datos de salida.Una función te permite 
 ##implementar operaciones que son habitualmente utilizadas en un programa y, de esta manera, reducir la cantidad de código.
 ## 2 tipos de funciones
 ## funciones propias de python
 print()##sirve para mostrar mensaje o resultado
 int()##esta funcion sirve para convertir string en entero
 input()##esta funcion sirve para pedir datos al usuario
 ##todo lo que se ingrese en input sera tomado como texto 

 ## funciones creadas
 ## creando funcion  
 def suma(a,b):
    resultado=a+b
    return resultado
## uso de funcion 
print(suma(4,6))
 
numero = int(input("Dígame cuántas palabras tiene la lista: "))

if numero < 1:
    print("¡Imposible!")
else:
    lista = []
    for i in range(numero):
        print("Dígame la palabra", str(i + 1) + ": ", end="")
        palabra = input()
        lista += [palabra]
     print("La lista creada es:", lista)

