def carga_de_articulos_kiosco(): #(punto A)
    lista_articulos = []
    codigo = input("Codigo articulo: ")
    refrigeracion = input("Refrigeracion(en caso de que el articulo necesite refrigeracion ingrese 'R', caso contrario 'N'): ")[0]
    while codigo != "999" or refrigeracion.lower() != "n":
        name_articulo = input("Nombre de articulo: ")
        descripcion = input("Descripcion: ")
        precio_de_venta = input("Precio de venta: ")
        name_proveedor = input("Nombre de proveedor: ")
        info_articulos = [codigo, refrigeracion, name_articulo, descripcion, precio_de_venta, name_proveedor]
        lista_articulos.append(info_articulos)
        codigo = input("Codigo articulo: ")
        refrigeracion = input("Refrigeracion(en caso de que el articulo necesite refrigeracion ingrese 'R', caso contrario 'N'): ")[0]
    return lista_articulos

#Imprime los datos de todos los articulos que necesitan refrigeracion o los que no la necesitan.(punto C)
def informacion_de_refrigeracion(lista):
    if len(lista)>0:
        consulta_refrigeracion = input("Para obtener datos de los articulos con refrigeracion ingrese R, caso contrario N: ")[0]
        for articulo in lista:
            refrigerar = articulo[1]
            
            if consulta_refrigeracion == refrigerar:
                print(articulo)
    else:
        pass

#Imprime la cantidad de articulos que necesitan refrigeracion y tambien la cantidad de las que no la necesitan.(punto D)
def cantidad_refrigeracion(lista):
    if len(lista)>0:
        cont_que_necesitan_refrigeracion = 0
        cont_sin_refrigeracion = 0
        for articulo in lista:
            refrigerar = articulo[1]
            
            if refrigerar == "r" or refrigerar == "R":
                cont_que_necesitan_refrigeracion += 1
            
            elif refrigerar == "n" or refrigerar == "N":
                cont_sin_refrigeracion +=1
        
        print("La cantidad de articulos que requieren refrigeracion es de: " + str(cont_que_necesitan_refrigeracion))   
        print("La cantidad de articulos que NO requieren refrigeracion es de: " + str(cont_sin_refrigeracion)) 
    
    else:
        pass

art = carga_de_articulos_kiosco()
print(art)
info_refrigeracion(art)
cantidad_refrigeracion(art)
        
        
