
arr=[
    {"Codigo": "C001","Nombre": "Pedro", "edad": 20, "NHijos":3},
    {"Codigo": "C002","Nombre": "Alberto", "edad": 68,"NHijos":4},
    {"Codigo": "C003","Nombre": "Jose Mendoza", "edad": 29,"NHijos":1},
    {"Codigo": "C004","Nombre": "Manuel", "edad": 59, "NHijos":2},
    {"Codigo": "C005","Nombre": "Miguel", "edad": 40, "NHijos":4},
    {"Codigo": "C006","Nombre": "Rigoberto", "edad": 82, "NHijos":5},
    {"Codigo": "C007","Nombre": "Pitter", "edad": 56, "NHijos":7},
    {"Codigo": "C008","Nombre": "Mario", "edad": 49, "NHijos":4},
    {"Codigo": "C009","Nombre": "Andres", "edad": 30, "NHijos":3},
    {"Codigo": "C0010","Nombre": "Luz", "edad": 61, "NHijos":1}
    ]

for i in arr:
  ##  print("Datos: ",i["Nombre"])
    sueldo_basico=1100
    adicional_hijos = sueldo_basico*0.2
    adicional_anciano = sueldo_basico*0.1

    if(i["edad"]>18 and i["edad"]<=50 and i["NHijos"]>3):
            i["sbasico"]=sueldo_basico+adicional_hijos

    elif(i["edad"] > 18 and i["edad"] <= 50):
            i["sbasico"]=sueldo_basico
    
    elif(i["edad"] > 50 and i["NHijos"] > 3):
            i["sbasico"]=sueldo_basico+adicional_anciano+adicional_hijos
    
    elif(i["edad"] > 50 and i["NHijos"] <= 3):
            i["sbasico"]=sueldo_basico+adicional_anciano

    else:
         i["sbasico"]=0
     
   # i["sbasico"]=1100
    print("Datos: ", i)



