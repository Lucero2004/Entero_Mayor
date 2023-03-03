#Verificar cual de los 2 numeros enteros es mayor
print("----------------------------------")
print("--------MAYOR DE 2 NUMEROS--------")
print("----------------------------------")

#input
A=int(input("Digite el primer número: "))
B=int(input("Digite el segundo numero: "))

#procesing
if(A>B):
    Mayor=A
else:
    Mayor=B

#output
print("----------------------------")
print("El número mayor es:" +str(Mayor))
print("-------------------------------------")        