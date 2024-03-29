import webbrowser
import os
from analisisLexico import tokens,palabras_reservadas,columnas,filas, erColumnas, erFilas,errores

def reporte():
    # Definir el contenido de la tabla en formato HTML
    tabla_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Reporte</title>
</head>
<body>
    <table border="1" cellborder="1" cellspacing="0" style="position: absolute; left: 0px;">
    <tr>
        <td>Token</td>
        <td>Lexema</td>
        <td>Filas</td>
        <td>Columna</td>           
    </tr>\n'''
    for i in range(len(tokens)):
        tabla_html += '''    <tr>
        <td>'''
        if tokens[i] == ":":
            tabla_html += "Dos puntos" 
        elif tokens[i] == "{":
            tabla_html += "Llave de apertura"
        elif tokens[i] == "}":
            tabla_html += "Llave de cierre"
        elif tokens[i] == ",":
            tabla_html += "Coma"  
        elif tokens[i] == "[":
            tabla_html += "Corchete de apertura"
        elif tokens[i] == "]":
            tabla_html += "Corchete de cierre" 
        elif tokens[i] not in palabras_reservadas:
            tabla_html += "Cadena"
        elif tokens[i] == '"':
            tabla_html += "Comilla" 
        elif tokens[i] == ';':
            tabla_html += "Punto y coma"   
        else:
            tabla_html += "Palabra reservada"
          
        tabla_html += '''</td>\n'''
        tabla_html +="        <td>"+ tokens[i]+"</td>\n"
        tabla_html +="        <td>"+str(filas[i])+"</td>\n"
        tabla_html +="        <td>"+str(columnas[i])+"</td>\n"
        tabla_html += '''    </tr>\n'''
    
    
    tabla_html+='''</table>\n'''
    
    tabla_html+='''<table border="1" cellborder="1" cellspacing="0" style="position: absolute; left: 50%;">\n'''
    tabla_html+='''    <tr>
        <td>Token</td>
        <td>Filas</td>
        <td>Columna</td>           
    </tr>\n'''
    i=0
    for i in range(len(errores)):
        tabla_html+='    <tr>\n'
        tabla_html+='       <td>'+errores[i]+'</td>\n'
        tabla_html+='       <td>'+erFilas[i]+'</td>\n'
        tabla_html+='       <td>'+erColumnas[i]+'</td>\n'
        tabla_html+='    </tr>\n'     
    tabla_html+='''</table>\n'''
    
    
    
    
    tabla_html+='''</body>\n</html>'''


    # Agregar el contenido HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/tabla.html", "w", encoding="utf-8") as f:
        f.write(tabla_html)

    # Abrir el archivo en el navegador
    ruta_absoluta = os.path.abspath("LFP_S1_2024_PROYECTO1_202100692/tabla.html")
    webbrowser.open("file://" + ruta_absoluta)
    