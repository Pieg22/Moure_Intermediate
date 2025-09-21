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
indicacion_Mayor_Diez = [comprobar for comprobar in aumento if comprobar > 10]
print(indicacion_Mayor_Diez)

# 9. Multiplica solo los nÃºmeros impares por 3 en una lista utilizando comprensiÃ³n.

# 10. Usa comprensiÃ³n de listas anidada para generar una matriz 3x3 con nÃºmeros del 1 al 9.