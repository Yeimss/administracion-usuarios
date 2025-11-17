from models.Usuario import Usuario

def main():
    objsebas  = Usuario("Sebas","Alzate","10249594","Girardota","Ingeniero")
    objjames  = Usuario("James","Herrera","100003434","Girardota","Desarrollador")
    
    objjames.presentarse()
    objsebas.presentarse()

    print(objjames.password)

    objjames.cambiar_contrasena()

    print(objjames.password)

if __name__ == "__main__": 
    main()