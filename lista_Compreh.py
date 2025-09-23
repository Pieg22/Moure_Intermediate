# 1. Genera una lista utilizando comprensiÃ³n con los nÃºmeros del 0 al 10.
llista = [0,1,2,3,4,5,6,7,8,9,10]
# 2. Crea una lista utilizando comprensiÃ³n con los cuadrados de los nÃºmeros del 1 al 10.
#[expresión for elemento in iterable ]
los_cuadrados = [i **2 for i in llista]
print(los_cuadrados)
# 3. Genera una lista utilizando comprensiÃ³n con los nÃºmeros pares del 0 al 20.
#[expresión for elemento in iterable if condición]
llista_parells = [i for i in range(0,21) if i % 2 == 0]
print(llista_parells)
# 4. Convierte una lista de temperaturas en Celsius a Fahrenheit utilizando comprensiÃ³n.
temperatures = [20 , 30 , 18]
#[expresión for elemento in iterable]
converter = [ i *9 /5 +32 for i in temperatures]
print(converter)
# 5. Crea una lista utilizando comprensiÃ³n con los caracteres de una cadena.
texto = "Ganesha"
caracteres = [letra for letra in texto]
print(caracteres)
# 6. Filtra una lista de palabras y deja solo las que tienen mÃ¡s de 4 letras utilizando comprensiÃ³n.
palabras = ["Hola","NihaoMa","Klk","Hello","Morning"]
filtro = [ palabra for palabra in palabras if len(palabra) >= 4]
print(filtro)
# 7. Aumenta en 5 cada nÃºmero de una lista con comprensiÃ³n usando una funciÃ³n externa.
def aumentar_en(numero):
     return numero + 5
aumento = [aumentar_en(i) for i in llista]
print(aumento)
# 8. Crea una lista de booleanos que indique si cada nÃºmero es mayor que 10 utilizando comprensiÃ³n.
indicacion_Mayor_Diez = [comprobar > 10 for comprobar in aumento ]
print(indicacion_Mayor_Diez)

# 9. Multiplica solo los nÃºmeros impares por 3 en una lista utilizando comprensiÃ³n.
multiplicacion = [ multi * 3 for multi in aumento if multi % 3 == 0]
print(multiplicacion)

# 10. Usa comprensiÃ³n de listas anidada para generar una matriz 3x3 con nÃºmeros del 1 al 9.
 #Repetir tomorrow

matriz_3x3 = [[(j * 3) + i for i in range(1, 4)] for j in range(3)]
print(matriz_3x3)


#for j in range(3) (rows) It makes a new sublist for the matrix (exterior loop)
#for i in range(1, 4) It makes the elements of each row 1,2,3 ofc . It runs 3 times for the exterior loop (interior loop)
#(j * 3) + i It make the operation ofc 

#Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 

def repeticion ():
     grupo_integrales = [] 
    
     while True :
          usuario_habla = input("Write numbers , then say done : ") # User write's
          if  usuario_habla.lower() == "done" : 
               break
          try :
           numero = int(usuario_habla) 
           grupo_integrales.append(numero)
           if numero >= 2 and numero <= 10 :
               grupo_integrales.append(numero)
           else:
               print("The number need to be betwen 2 and 10")
          except ValueError:
           print("Invalid Input")   
     if grupo_integrales :
         minimo = min(grupo_integrales)
         maximo = max(grupo_integrales)
         print(f"{minimo} this is the lower one , and {maximo} is bigger")
     else : 
         print("We need numbers!")
     
     
     
repeticion()
# Once 'done' is entered, print out the largest and smallest of the numbers.
# If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below:
#Invalid input
#Maximum is 10
#Minimum is 2