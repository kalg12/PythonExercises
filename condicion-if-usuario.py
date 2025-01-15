#En este ejercicio vamos a validar un usuario y contraseña de un usuario
#Si el usuario es correcto y la contraseña es correcta,
# entonces se imprime un mensaje de bienvenida

#Se pide al usuario que ingrese su usuario
usuario = input("Ingrese su usuario: ")

#Se pide al usuario que ingrese su contraseña
contraseña = input("Ingrese su contraseña: ")

#Se valida si el usuario es igual a "admin" y la contraseña es igual a "admin123"
if usuario == "admin" and contraseña == "admin123":
    print("Bienvenido al sistema")
else:
    print("Usuario o contraseña incorrecta")