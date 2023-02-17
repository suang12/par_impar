#Programa para saber si un numeo es par o impar 

print("--------------------------------")
print("------ INGRESE UN NUMERO -------")
print("--------------------------------")

#input
x = int(input("INGRESE UN NÚMERO: "))

#processing
r = (x % 2)
if r==0:
    msj="PAR"
else:
    msj="IMPAR"


# output
print("---------------------------------")
print("----------- RESULTADO -----------")
print("---------------------------------")


print(" EL NÚMERO " + str(x) + " es " + msj)

    