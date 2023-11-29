comando = ""
count = 0

data = [
    {"id": 1, "nombres": "Manuel Arturo","apellidos": "Peralta Saavedra","edad": 25,"username": "marturop","password": "123456789"},
    {"id": 2, "nombres": "Pedro","apellidos": "Rivera","edad": 20,"username": "privera","password": "123456789"}
    ]

while(comando != "exit"):

    comando = input("Ingrese una opción: ")
    print("comando: ", comando)

    if(comando == "exit"):
        print("Hasta pronto")
        break

    if(comando == "login"):
        username=input("Ingrese el username: ")
        password=input("ingrese el password: ")

        for i in data:
                if( i['username'] == username and i['password'] == password):      
                    print("Login exitoso")
                    print("data: ", i)
                else:
                    print("data: ", i)
                    print("usuario o contraseña son incorrectas")
                    

    else:
        nombres= input("Ingrese los nombres del usuario: ")
        apellidos=input("Ingrese los apellidos del usuario: ")
        edad = int(input("Ingrese su edad: "))
        username=input("Ingrese el username: ")
        password=input("ingrese el password: ")
        verify_password=input("vuelva a ingresar el password: ")

        if( password == verify_password):
            for i in data:
                count = i['id']+1
            

            data.insert(count, {'id': count})
            for i in data:
                if(i['id'] == count):
                    i['id'] = count
                    i['nombres'] = nombres
                    i['apellidos'] = apellidos
                    i['edad'] = edad
                    i['username'] = username
                    i['password'] = password
                    print("new data: ", data)
        
        else:
            print("contraseñas no coinciden")

       
