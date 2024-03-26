import webbrowser
import os
from analisisLexico import tokens,palabras_reservadas,columnas,filas

def reporte():
    # Definir el contenido de la tabla en formato HTML
    tabla_html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reporte</title>
    </head>
    <body>
    <table border="1" cellborder="1" cellspacing="0">
        <tr>
            <td>Token</td>
            <td>Lexema</td>
            <td>Filas</td>
            <td>Columna</td>           
        </tr>
    '''
    for i in range(len(tokens)):
        tabla_html +='''
        <tr>
            <td>'''
        if tokens[i]==":":
           tabla_html +="Dos puntos" 
        if tokens[i]=="{":
            tabla_html +="Llave de apertura"
        if tokens[i]=="}":
            tabla_html +="Llave de cierre"
        if tokens[i]==",":
            tabla_html +="Coma"  
        if tokens[i]=="[":
            tabla_html +="Corchete de apertura"
        if tokens[i]=="]":
            tabla_html +="Corchete de cierre" 
        if tokens[i] not in palabras_reservadas:
            tabla_html += "Cadena"
        else:
            tabla_html += "Palabra reservada"
        if tokens[i]=='"':
            tabla_html +="Comilla" 
        if tokens[i]==';':
            tabla_html +="Punto y coma"   
        tabla_html +='''
            </td>\n'''
        tabla_html +='''
            <td>'''
        tabla_html +="          "+tokens[i]
        tabla_html +='''
            </td>\n'''
        tabla_html +='''
            <td>'''
        tabla_html +="          "+str(filas[i])       
        tabla_html +='''
            <td>\n'''
        tabla_html +="          "+columnas[i]
        tabla_html +='''
            </td>\n'''
        tabla_html +='''
        </tr>'''
    tabla_html+='''
        </table>
    </body>
</html>
    
'''


    # Agregar el contenido HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/tabla.html", "w", encoding="utf-8") as f:
        f.write(tabla_html)

    # Abrir el archivo en el navegador
    ruta_absoluta = os.path.abspath("LFP_S1_2024_PROYECTO1_202100692/tabla.html")
    webbrowser.open("file://" + ruta_absoluta)
    