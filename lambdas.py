# 1. Crea una lambda que sume dos nÃºmeros.
sumar = lambda primer_numero , segundo_numero : primer_numero + segundo_numero 
print(sumar(100,3000))

# 2. Crea una lambda que calcule el cuadrado de un nÃºmero.
cuadrado = lambda first_n , second_n : first_n ** second_n
print(cuadrado(32,10))

# 3. Crea una lambda que devuelva el mayor de dos nÃºmeros.
el_mayor = lambda w,z : w if w > z else z 
print(el_mayor(100,300))
print(el_mayor(68,11))

# 4. Crea una lambda que sume 10 a un nÃºmero dado.
otra_suma = lambda k : k +10
print(otra_suma(10))

# 5. Crea una lambda que devuelva el Ãºltimo carÃ¡cter de una cadena.

ultimo = lambda cadena : cadena[-1]
print(ultimo("Perrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrra"))

# 6. Crea una lambda que indique si una palabra tiene mÃ¡s de 6 letras.
mas_de_seis = lambda letras : len(letras) > 6 
print(mas_de_seis("Have more than 6 leters ? ")) 

# Ejemplo Gemini interesante : Devuelve texto en lugar de un booleano
mensaje_lambda = lambda letras: "Sí, tiene muchas letras" if len(letras) > 6 else "No, tiene 6 o menos"
                                # valor_si_verdadero         condición             valor_si_false 
print(mensaje_lambda("Testing"))  # Salida: Sí, tiene muchas letras
print(mensaje_lambda("Hello"))    # Salida: No, tiene 6 o menos

# 7. Crea una lambda que convierta una cadena a minÃºsculas.
minus = lambda l : str.lower(l)
print(minus("MAYUS"))

# 8. Crea una lambda que devuelva True si un nÃºmero es positivo.

positivo = lambda positive_number : positive_number > 0
print(positivo(900000000000000))  

# 9. Crea una lambda que devuelva "Cadena vacÃ­a" si el string estÃ¡ vacÃ­o.
empty_string = lambda cadena_empty : "Cadena vacía" if cadena_empty == "" else "No esta vacía"
print(empty_string(""))

# 10. Crea una lambda que calcule el precio final con un impuesto aÃ±adido del 21%.
final_price = lambda precio, result  : precio if 
print(final_price(100)) 