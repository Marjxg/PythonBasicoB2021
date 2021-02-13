print("Bienvenido al programa")
Contraseña = "perritos123"
print("Introduzca la contraseña: ", end="")
Password = input()
Password = Password.lower()

if Password == Contraseña:
    print("Contraseña correcta.")
else: 
    print("Contraseña incorrecta.")
