palabras_reservadas = ["Inicio", 
                       "Encabezado", 
                       "TituloPagina", 
                       "Cuerpo",
                       "Titulo", 
                       "Fondo", 
                       "Parrafo", 
                       "Texto", 
                       "Codigo", 
                       "Negrita", 
                       "Subrayado", 
                       "Tachado", 
                       "Cursiva", 
                       "Salto", 
                       "Tabla"]
tokens=[]
caracteres=[]


# Función para cargar el archivo .txt
def cargar_archivo_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()
    return contenido

def convertir_a_html(contenido):   
    html='''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>
    '''
    
    for linea in contenido:
        linea_sin_sangria = linea.strip()  # Eliminar espacios en blanco al inicio y al final de la línea
        if linea_sin_sangria[0:6] == palabras_reservadas[0]:
            tokens.append(palabras_reservadas[0])
            for i in range(6, len(linea_sin_sangria)):
                tokens.append(linea_sin_sangria[i])
        if linea_sin_sangria[0:10] == palabras_reservadas[1]:
            tokens.append(palabras_reservadas[1])
            for i in range(10, len(linea_sin_sangria)):
                tokens.append(linea_sin_sangria[i])
        if linea_sin_sangria[0:12] == palabras_reservadas[2]:
            if linea_sin_sangria.startswith(palabras_reservadas[2]):
                tokens.append(palabras_reservadas[2])
                tokens.append(linea_sin_sangria[12])  # Agregar el primer carácter después de la coincidencia
                tokens.append(linea_sin_sangria[13])  # Agregar el segundo carácter después de la coincidencia
                tokens.append(linea_sin_sangria[14:-2])  # Agregar los caracteres restantes después de la coincidencia
                tokens.append(linea_sin_sangria[-2])  # Agregar el penúltimo carácter de la línea
                tokens.append(linea_sin_sangria[-1])  # Agregar el último carácter de la línea
        if linea_sin_sangria[0:6] == palabras_reservadas[3]:
            tokens.append(palabras_reservadas[3])
            for i in range(6, len(linea_sin_sangria)):
                tokens.append(linea_sin_sangria[i])
        if linea_sin_sangria[:6] == palabras_reservadas[4]:
            tokens.append(palabras_reservadas[4])
            

        
        
        
        
        
        
        
        #if linea_sin_sangria[0] == "}":
        #    tokens.append("}")
        #if linea_sin_sangria[0] == "]":
        #    tokens.append("]")
        #if len(linea_sin_sangria) >= 2 and (linea_sin_sangria[0] == "," or linea_sin_sangria[1] == ","):
        #    tokens.append(",")
                


  
    print(tokens)
   
        
    html+='''
    </html lang="en">
    '''
    
    
    # Guardamos el HTML en un archivo
    with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", "w", encoding="utf-8") as archivo_html:
        archivo_html.write(html)
        


archivo_txt = "LFP_S1_2024_PROYECTO1_202100692\entrada.txt"
contenido = cargar_archivo_txt(archivo_txt)
convertir_a_html(contenido)