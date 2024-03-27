from analisisLexico import tokens


def hacerHtml():
    tituloHead=""
    titulo = []
    fondo=[]
    parrafo=[]
    texto=[]
    codigo=[]
    negrita=[]
    subrayado=[]
    tachado=[]
    cursiva=[]
    salto=[]
    tabla=[]
    
    html="<!DOCTYPE html>\n"'''<html lang="en">\n'''+"<head>\n"
    html+='''    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>'''
    
    for i in range(len(tokens)):
        if tokens[i]=="TituloPagina":
            tituloHead=tokens[i+3]
    html+=tituloHead+"</title>\n</head>\n<body>\n"
    
    for i in range(len(tokens)):
        if tokens[i] == "Titulo":
            j = i + 1
            atributos = {}  # Diccionario para almacenar los atributos del título de forma dinámica
            while j < len(tokens) and tokens[j] != "}":
                # Comprobar si el token actual es un atributo válido del título
                if tokens[j] in ["texto", "posicion", "tamaño", "color"]:
                    # Añadir el atributo y su valor al diccionario de atributos
                    atributos[tokens[j]] = tokens[j + 3]
                j += 1
            # Agregar los valores del diccionario a la lista de título
            titulo.append([atributos.get("texto", ""), 
                           atributos.get("posicion", ""), 
                           atributos.get("tamaño", ""), 
                           atributos.get("color", "")])
        if tokens[i] == "Fondo" and tokens[i+3]=="color":
            fondo.append(tokens[i+6])
        if tokens[i] == "Parrafo":
            j = i + 1
            atributos = {}  # Diccionario para almacenar los atributos del título de forma dinámica
            while j < len(tokens) and tokens[j] != "}":
                # Comprobar si el token actual es un atributo válido del título
                if tokens[j] in ["texto", "posicion"]:
                    # Añadir el atributo y su valor al diccionario de atributos
                    atributos[tokens[j]] = tokens[j + 3]
                j += 1
            # Agregar los valores del diccionario a la lista de título
            parrafo.append([atributos.get("texto", ""), 
                           atributos.get("posicion", "")])
        if tokens[i] == "Texto":
            j = i + 1
            atributos = {}  # Diccionario para almacenar los atributos del título de forma dinámica
            while j < len(tokens) and tokens[j] != "}":
                # Comprobar si el token actual es un atributo válido del título
                if tokens[j] in ["fuente", "color","tamaño"]:
                    # Añadir el atributo y su valor al diccionario de atributos
                    atributos[tokens[j]] = tokens[j + 3]
                j += 1
            # Agregar los valores del diccionario a la lista de título
            texto.append([atributos.get("fuente", ""), 
                           atributos.get("color", ""),
                           atributos.get("tamaño", "")])
        if tokens[i] == "Codigo":
            j = i + 1
            atributos = {}  # Diccionario para almacenar los atributos del título de forma dinámica
            while j < len(tokens) and tokens[j] != "}":
                # Comprobar si el token actual es un atributo válido del título
                if tokens[j] in ["texto", "posicion"]:
                    # Añadir el atributo y su valor al diccionario de atributos
                    atributos[tokens[j]] = tokens[j + 3]
                j += 1
            # Agregar los valores del diccionario a la lista de título
            codigo.append([atributos.get("texto", ""), 
                           atributos.get("posicion", "")])   
        if tokens[i] == "Negrita":
            negrita.append(tokens[i+6])
        if tokens[i] == "Subrayado":
            subrayado.append(tokens[i+6])
        if tokens[i] == "Tachado":
            tachado.append(tokens[i+6])
        if tokens[i] == "Cursiva":
            cursiva.append(tokens[i+6])
        if tokens[i] == "Salto":
            salto.append(tokens[i+6])
        if tokens[i] == "Tabla":
            tabla.append(tokens[i+6])
            
                    
    
    html+="</body>\n</html>" 
    print(titulo)
    print(fondo)
    print(parrafo)
    print(texto)
    print(codigo)
    print(negrita)
    print(subrayado)
    print(tachado)
    print(cursiva)
    print(salto)
     
        
    # Guardamos el HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write(html)