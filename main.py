#PRIMER Y SEGUNDO EJERCICIO: Al principio le pediremos un número cualquiera e indetificaremos con que tipo de variable está trabajando. Posteriormente, le pedimos dos números al usuario y mostramos que tipo de variable es. En el primer número la variable es de tipo "INT" y en el segundo de tipo "FLOAT", es decir, es decimal. Posteriormente, al primer número le hemos insertado 5 ceros delante; para elllo necesitamos referirnos al número y usar la función ".zfill" para indicar los 0 que queremos. Para el número decimal hemos usado un "format" para referirnos a la variable y "{:.nf}" para indicar cuantos decimales imprimirá por pantalla, donde n denota la cantidad.

num=input("Introduce un número cualquiera:")
print(type(num))
print("\n\n")

num1 = int(input("Escribe el primer número: "))
print(type(num1))
print("\n\n")

num2 = float(input("Escribe el segundo número: "))
print(type(num2))
print("\n\n")

print(str(num1).zfill(5+len(str(num1))))
print("\n")

print("{:09.03f}".format(num2))
print("\n\n\n")


#TERCER EJERCICIO: En este ejercicio sencillamente utilizaremos la valirbale format, de tal manera que, con pequeños cambios en el código podemos escribir el mismo mensaje con menos trabajo y haciendo referencia a las variables entre {}

altura = float(input("Cuanto mides en metros?: "))
peso= float(input("Cúal es tu peso en kilogramos?: "))
print("\n")

print("Tu altura es {0} metros y tu peso es de {1} KG".format(altura, peso))
print("\n")

print("Tu altura es {1} metros y tu peso es de {0} KG".format(peso, altura))
print("\n")

print("Tu altura es de {0:<5} metros y tu peso es de {1:>5} KG".format(altura, peso))
print("\n")









