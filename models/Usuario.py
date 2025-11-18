from utils.PasswordUtils import aplicar_reglas_contrasena

class Usuario:
    def __init__(self, nombre, apellido, documento, ciudad, profesion):
        self.nombre = nombre
        self.apellido = apellido
        self.documento = documento
        self.ciudad = ciudad
        self.profesion = profesion
        self.password = "1234"

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y vivo en {self.ciudad}")

    def cambiar_contrasena(self):
        if not self.validar_contrasena_actual():
            return
        
        self.obtener_nueva_contrasena()

    def validar_contrasena_actual(self):
        contrasena = input("Ingrese contraseña actual: ")

        if contrasena != self.password:
            print("Contraseña incorrecta")
            return False
        
        return True

    def obtener_nueva_contrasena(self):
        while True:
            nueva = input("Ingrese nueva contraseña: ")
            validar = input("Ingrese nuevamente contraseña: ")

            if nueva != validar:
                print("No coincide. Inténtelo nuevamente.\n")
                continue

            if not aplicar_reglas_contrasena(nueva):
                print("La contraseña no cumple las reglas.\n")
                continue

            self.password = nueva
            print("Contraseña cambiada exitosamente.")
            break
