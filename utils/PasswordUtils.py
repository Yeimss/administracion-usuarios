def validar_mayuscula(string) -> bool:
        tiene_mayuscula = any(c.isupper() for c in string)
        return tiene_mayuscula

def validar_minuscula(string) -> bool:
    tiene_minuscula = any(c.isupper() for c in string)
    return tiene_minuscula

def validar_signo(string) -> bool:
    caracteres_especiales = "!@#$%^&*()-_=+[]{};:'\",.<>?/\\|`~"
    tiene_caracter_especial = any(c in caracteres_especiales for c in string)
    return tiene_caracter_especial


def aplicar_reglas_contrasena(password:str):
    mensaje = ""
    if len(password) <= 5:
        mensaje += "\n* La contraseña debe tener más de 5 dígitos"
    if validar_mayuscula(password):
        mensaje += "\n* La contraseña debe tener al menos una mayuscula"
    if validar_minuscula(password):
        mensaje += "\n* La contraseña debe tener al menos una minuscula"
    if validar_signo(password):
        mensaje += "\n* La contraseña debe tener al menos un simbolo"
    
    valido = False
    if len(mensaje) == 0:
        mensaje = "Contraseña válida."
        valido = True

    print(mensaje)
    return valido