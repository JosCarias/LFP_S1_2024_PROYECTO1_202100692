from analisisLexico import tokens
import webbrowser
import os


def hacerHtml():
    tituloHead=""
    titulo = []
    fondo=[]
    parrafo=[]
    txt=[]
    codigo=[]
    negrita=[]
    subrayado=[]
    tachado=[]
    cursiva=[]
    salto=[]
    tabla=[]
    elementos=[]
    
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
            txt.append([atributos.get("fuente", ""), 
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
        if tokens[i] == "elemento":
            aux=[]
            fila=tokens[i+8]
            columna=tokens[i+16]
            texto=tokens[i+20]
            aux.append(fila)
            aux.append(columna)
            aux.append(texto)
            elementos.append(aux)  
            
        
    
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
        if posicion == "derecha":
            estilo += 'position: absolute; left: 100%; transform: translateX(-100%);'
        if posicion == "centro":
            estilo += 'position: absolute; left: 50%; transform: translateX(-50%);'

        # Establecer el estilo de acuerdo al tamaño
        if tamaño == "t1":
            estilo += 'font-size: 30px;'  # Tamaño grande
        elif tamaño == "t2":
            estilo += 'font-size: 25px;'  # Tamaño mediano grande
        elif tamaño == "t3":
            estilo += 'font-size: 20px;'  # Tamaño medio
        elif tamaño == "t4":
            estilo += 'font-size: 15px;'  # Tamaño mediano pequeño
        elif tamaño == "t5":
            estilo += 'font-size: 12px;'  # Tamaño pequeño
        elif tamaño == "t6":
            estilo += 'font-size: 10px;'  # Tamaño muy pequeño
        else:
            estilo += 'font-size:'+tamaño+"px;"  # Tamaño personali

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
        html += '   <div style="' + estilo + '">' + lista[0] + '</div>\n    <br>\n'
    
    for lista in parrafo:
        estilo=""
        posicion=lista[1] 
        # Establecer el estilo de acuerdo a la posición
        if posicion == "izquierda":
            estilo += 'position: absolute; left: 0px;'
        if posicion == "derecha":
            estilo += 'position: absolute; left: 100%; transform: translateX(-100%);'
        if posicion == "centro":
            estilo += 'position: absolute; left: 50%; transform: translateX(-50%);' 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <p style="' + estilo + '">' + lista[0] + '</p>\n    <br>\n'  
        
    for lista in txt:
        estilo = "position: absolute;"
        fuente = lista[0]
        color = lista[1]
        tamaño = lista[2]
        estilo += "font-family: '" + fuente + "';"
    
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
        html += '   <p style="' + estilo + '">' + "Atributo a texto" + '</p>\n  <br>\n'
    
    for lista in codigo:
        estilo="font-family: 'Times New Roman', serif;"
        posicion=lista[1] 
        # Establecer el estilo de acuerdo a la posición
        if posicion == "izquierda":
            estilo += 'position: absolute; left: 0px;'
        if posicion == "derecha":
            estilo += 'position: absolute; left: 100%; transform: translateX(-100%);'
        if posicion == "centro":
            estilo += 'position: absolute; left: 50%; transform: translateX(-50%);' 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <p style="' + estilo + '">' + lista[0] + '</p>\n    <br>\n' 
    
    for lista in negrita:
        estilo="" 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <b style="' + estilo + '">' + lista + '</b>\n   <br>\n'  
    
    for lista in subrayado:
        estilo="" 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <u style="' + estilo + '">' + lista + '</u>\n   <br>\n' 
    
    for lista in tachado:
        estilo="" 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <s style="' + estilo + '">' + lista+ '</s>\n    <br>\n' 
    
    for lista in cursiva:
        estilo="" 
        # Agregar el div al HTML con el estilo aplicado
        html += '   <i style="' + estilo + '">' + lista + '</i>\n   <br>\n'
    
    for lista in salto:
        estilo="" 
        i=0
        for i in range(int(lista[0])):           
            # Agregar el div al HTML con el estilo aplicado
            html += '   <br>\n' 
       
    for lista in tabla:
        html += '''   <table border="1" cellborder="1" cellspacing="0">\n'''
        filas = int(lista[0])
        columnas = int(lista[1])
        
        for i in range(filas):
            html += "   <tr>\n"
            for j in range(columnas):
                elemento_encontrado = False
                for elemento in elementos:
                    if i+1 == int(elemento[0]) and j+1 == int(elemento[1]):
                        html += "   <td>" + elemento[2] + "</td>\n"
                        elemento_encontrado = True
                        break
                    
                if not elemento_encontrado:
                    html += "   <td></td>\n"  # Insertar una celda en blanco
                    
            html += "   </tr>\n"
        
        html += "   </table>\n    <br>\n"
                    
    
    html+="</body>\n</html>"     
        
    
    # Guardamos el HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write(html)
        
    # Abrir el archivo en el navegador
    ruta_absoluta = os.path.abspath("LFP_S1_2024_PROYECTO1_202100692/resultado.html")
    webbrowser.open("file://" + ruta_absoluta)