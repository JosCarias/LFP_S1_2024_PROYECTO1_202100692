from analisisLexico import tokens


def hacerHtml():
    tituloHead=""
    titulo = []
    fondo=[]
    
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
            

            
                    
    
    html+="</body>\n</html>" 
    print(titulo)
    print(fondo)
        
    # Guardamos el HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write(html)