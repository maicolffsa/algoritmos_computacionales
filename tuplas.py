"Tuplas" 
 Tpl = (12, "Hola", 6.8, "Zegel", 1000)
print(Tpl)

"Agregar items a una tupla"
Tpl2 = Tpl + (999, "Ipae")
print("tuplas agregadas", Tpl2)

"Multiplicar Tuplas"
Tpl3 = Tpl*3
print("Tuplas multiplicadas", Tpl3) 

"Diccionario"
dicc={"id": 11, "Nombre": "Jose", "Apellido": "Perez", "Telefono": "947896321", "Correo": "prueba@gmail.com"}
print("resultado diccionario: ",dicc['Nombre']) 

"Lista"
lista = [{"id": 11, "Nombre": "Jose", "Apellido": "Perez"},2,3,4,5,6] 

dicc={"id": 11, "Nombre": "Jose", "Apellido": "Perez", "Telefono": "947896321", "Correo": "prueba@gmail.com"}

"Agregar datos al diccionario"
dicc["Lugar_de_Residencia"]="Cuzco"
print(dicc["Lugar_de_Residencia"])


"Listado de datos de un diccionario"
for valor in dicc.items():
    print(valor)
 
"Edición de Datos de un diccionario"
dicc["Correo"]="micorreo@zegel.edu.pe"
print(dicc["Correo"])


"Eliminación de Datos de un diccionario"

del dicc["Telefono"]


