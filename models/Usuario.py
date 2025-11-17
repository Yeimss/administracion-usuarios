class Usuario:
    def __init__(self,name,lastname,id,city,profession):
        self.nombre = name
        self.apellido = lastname
        self.documento = id
        self.ciudad = city
        self.profesion = profession
        self.password = "1234"

    def presentarse(self):
        print(f"Hola mi nombre es {self.nombre} y vivo en {self.ciudad}")

    def cambiar_contrasena(self):

        contrasena_anterior = input("Ingrese contraseña actual: ")
        
        if contrasena_anterior == self.password:

            nueva_contrasena = input("Ingrese nueva contraseña: ")
            validacion_nueva_contra = input("Ingrese nuevamente contraseña: ")

            if nueva_contrasena == validacion_nueva_contra:

                self.password = nueva_contrasena

                print("Contraseña cambiada")

            else:
                print("No coincide")
        
        else:
            print("Contraseña incorrecta")



    







