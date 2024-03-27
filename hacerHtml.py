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
            
    html+=tituloHead+"</title>\n</head>\n"
    
    
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
            j = i + 1
            atributos = {}  # Diccionario para almacenar los atributos del título de forma dinámica
            while j < len(tokens) and tokens[j] != "}":
                # Comprobar si el token actual es un atributo válido del título
                if tokens[j] in ["filas", "columnas"]:
                    # Añadir el atributo y su valor al diccionario de atributos
                    atributos[tokens[j]] = tokens[j + 3]
                j += 1
            # Agregar los valores del diccionario a la lista de título
            tabla.append([atributos.get("filas", ""), 
                           atributos.get("columnas", "")])
    
    for lista in fondo:
        estilo = ""
        # Establecer el estilo de acuerdo al color de fondo
        if lista == "rojo":
            estilo += 'background-color: red;'
        elif lista == "amarillo":
            estilo += 'background-color: yellow;'
        elif lista == "azul":
            estilo += 'background-color: blue;'
        else:
            estilo += 'background-color: ' + lista + ';'
        html += '<body style="' + estilo + '">' + '\n'
    
     
    for lista in titulo:
        estilo = ""
        posicion = lista[1]
        tamaño = lista[2]
        color = lista[3]

        # Establecer el estilo de acuerdo a la posición
        if posicion == "izquierda":
            estilo += 'position: absolute; left: 0px;'
        elif posicion == "derecha":
            estilo += 'position: absolute; right: 0;'
        elif posicion == "centro":
            estilo += 'position: absolute; left: 50%; transform: translateX(-50%);'

        # Establecer el estilo de acuerdo al tamaño
        if tamaño == "t1":
            estilo += 'font-size: 30px;'
        elif tamaño == "t2":
            estilo += 'font-size: 25px;'
        elif tamaño == "t3":
            estilo += 'font-size: 20px;'
        elif tamaño == "t4":
            estilo += 'font-size: 15px;'
        elif tamaño == "t5":
            estilo += 'font-size: 12px;'
        elif tamaño == "t6":
            estilo += 'font-size: 10px;'

        # Establecer el estilo de acuerdo al color
        if color == "rojo":
            estilo += 'color: red;'
        elif color == "amarillo":
            estilo += 'color: yellow;'
        elif color == "azul":
            estilo += 'color: blue;'
        else:
            estilo += 'color: ' + color + ';'

        # Agregar el div al HTML con el estilo aplicado
        html += '   <div style="' + estilo + '">' + lista[0] + '</div>\n'
    
    for lista in parrafo:
        estilo=""
        texto=lista[0]
        posicion=lista[1] 
        # Establecer el estilo de acuerdo a la posición
        if posicion == "izquierda":
            estilo += 'position: absolute; left: 0px;'
        elif posicion == "derecha":
            estilo += 'position: absolute; right: 0;'
        elif posicion == "centro":
            estilo += 'position: absolute; left: 50%; transform: translateX(-50%);' 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <p style="' + estilo + '">' + lista[0] + '</p>\n'  
            
                    
    
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
    print(tabla)
     
        
    # Guardamos el HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write(html)