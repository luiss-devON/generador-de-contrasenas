import secrets
import string

def generar_contrasena(largo=16, simbolos=True):
    caracteres = string.ascii_letters + string.digits
    if simbolos:
        caracteres += "!@#$%&*?"
    return "".join(secrets.choice(caracteres) for _ in range(largo))

print("=== Generador de contraseñas ===")

 
while True:
    try:
        largo = int(input("¿Cuántos caracteres? (mínimo 8): "))
        break
    except ValueError:
        print("Eso no es un número, intenta de nuevo.")

if largo < 8:
    print("Muy corta, usaremos 8.")
    largo = 8

 
while True:
    respuesta = input("¿Incluir símbolos? (s/n): ").lower()
    if respuesta in ("s", "n"):
        break
    print("Escribe solo s o n.")

usar_simbolos = respuesta == "s"

print("Tu contraseña:", generar_contrasena(largo, usar_simbolos))