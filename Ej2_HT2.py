print("Bienvenido al programa")
print("Por favor, ingrese su nombre: ", end="")
nombre = input()

print("Por favor, ingrese su género: ", end="")
género = input()

if género == "F":
    if nombre.upper() < "M":
        grupo = "A"
    else:
        grupo = "B" 

else:
    if nombre.upper() > "N":
        grupo = "A"
    else:
        grupo = "B" 

print("Su grupo es: " + grupo)



