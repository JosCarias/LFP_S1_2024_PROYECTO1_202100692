tokens=[]
columnas=[]
filas=[]
palabras_reservadas = ["Inicio", 
                       "Encabezado", 
                       "TituloPagina", 
                       "Cuerpo",
                       "Titulo",  
                       "texto", 
                       "posicion", 
                       "tamaño",
                       "color",
                       "Fondo",
                       "Parrafo",
                       "Texto",
                       "fuente",
                       "Codigo",
                       "Negrita",
                       "Subrayado",
                       "Tachado",
                       "Cursiva",
                       "Salto",
                       "cantidad",
                       "Tabla",
                       "filas",
                       "columnas",
                       "elemento",
                       "fila",
                       "columna"                       
                       ]

# Función para cargar el archivo .txt
def cargar_archivo_txt(ruta):
    with open(ruta, 'r', encoding='utf-8') as archivo:
        contenido = archivo.readlines()
    return contenido

def analizador(contenido): 
    i=1
    j=1
    for linea in contenido:
        linea_sin_sangria = linea.strip()  # Eliminar espacios en blanco al inicio y al final de la línea  
        if linea_sin_sangria[0:6] == palabras_reservadas[0] and linea_sin_sangria[6]==":": #Inicio
            tokens.append(palabras_reservadas[0])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i)) 
                filas.append(j)      
        if linea_sin_sangria[0:10] == palabras_reservadas[1] and linea_sin_sangria[10]==":": #Encabezado
            tokens.append(palabras_reservadas[1])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:12] == palabras_reservadas[2] and linea_sin_sangria[12]==":": #TituloPagina
            tokens.append(palabras_reservadas[2])
            tokens.append(linea_sin_sangria[12])  # Agregar el primer carácter después de la coincidencia
            tokens.append(linea_sin_sangria[13])  # Agregar el segundo carácter después de la coincidencia
            tokens.append(linea_sin_sangria[14:-2])  # Agregar los caracteres restantes después de la coincidencia
            tokens.append(linea_sin_sangria[-2])  # Agregar el penúltimo carácter de la línea
            tokens.append(linea_sin_sangria[-1])  # Agregar el último carácter de la línea
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:6] == palabras_reservadas[3] and linea_sin_sangria[6]==":": #Cuerpo
            tokens.append(palabras_reservadas[3])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:6] == palabras_reservadas[4] and linea_sin_sangria[6]==":":  #Titulo
            tokens.append(palabras_reservadas[4])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[5] and linea_sin_sangria[5]==":":  #texto
            tokens.append(palabras_reservadas[5])
            tokens.append(linea_sin_sangria[5])
            tokens.append(linea_sin_sangria[6])
            tokens.append(linea_sin_sangria[7:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i)) 
                filas.append(j)
        if linea_sin_sangria[0:8] == palabras_reservadas[6] and linea_sin_sangria[8]==":":  #posicion
            tokens.append(palabras_reservadas[6])
            tokens.append(linea_sin_sangria[8])
            tokens.append(linea_sin_sangria[9])
            tokens.append(linea_sin_sangria[10:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i)) 
                filas.append(j)
        if linea_sin_sangria[0:6] == palabras_reservadas[7] and (linea_sin_sangria[6]==":" or linea_sin_sangria[6]=="="):  #tamaño
            tokens.append(palabras_reservadas[7])
            tokens.append(linea_sin_sangria[6])
            tokens.append(linea_sin_sangria[7])
            tokens.append(linea_sin_sangria[8:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[8] and (linea_sin_sangria[5]==":" or linea_sin_sangria[5]=="="):  #color
            tokens.append(palabras_reservadas[8])
            tokens.append(linea_sin_sangria[5])
            tokens.append(linea_sin_sangria[6])
            tokens.append(linea_sin_sangria[7:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[9] and linea_sin_sangria[5]==":":  #Fondo
            tokens.append(palabras_reservadas[9])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:7] == palabras_reservadas[10] and linea_sin_sangria[7]==":":  #Parrafo
            tokens.append(palabras_reservadas[10])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[11] and linea_sin_sangria[5]==":":  #Texto
            tokens.append(palabras_reservadas[11])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:6] == palabras_reservadas[12] and linea_sin_sangria[6]=="=":  #fuente
            tokens.append(palabras_reservadas[12])
            tokens.append(linea_sin_sangria[6])
            tokens.append(linea_sin_sangria[7])
            tokens.append(linea_sin_sangria[8:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:6] == palabras_reservadas[13] and linea_sin_sangria[6]==":":  #Codigo
            tokens.append(palabras_reservadas[13])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:7] == palabras_reservadas[14] and linea_sin_sangria[7]==":":  #Negrita
            tokens.append(palabras_reservadas[14])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:9] == palabras_reservadas[15] and linea_sin_sangria[9]==":":  #Subrayado
            tokens.append(palabras_reservadas[15])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:7] == palabras_reservadas[16] and linea_sin_sangria[7]==":":  #Tachado
            tokens.append(palabras_reservadas[16])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:7] == palabras_reservadas[17] and linea_sin_sangria[7]==":":  #Cursiva
            tokens.append(palabras_reservadas[17])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[18] and linea_sin_sangria[5]==":":  #Salto
            tokens.append(palabras_reservadas[18])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:8] == palabras_reservadas[19] and linea_sin_sangria[8]==":":  #cantidad
            tokens.append(palabras_reservadas[19])
            tokens.append(linea_sin_sangria[8])
            tokens.append(linea_sin_sangria[9])
            tokens.append(linea_sin_sangria[10:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[20] and linea_sin_sangria[5]==":":  #Tabla
            tokens.append(palabras_reservadas[20])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(3):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:5] == palabras_reservadas[21] and linea_sin_sangria[5]==":":  #filas
            tokens.append(palabras_reservadas[21])
            tokens.append(linea_sin_sangria[5])
            tokens.append(linea_sin_sangria[6])
            tokens.append(linea_sin_sangria[7:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:8] == palabras_reservadas[22] and linea_sin_sangria[8]==":":  #columna
            tokens.append(palabras_reservadas[22])
            tokens.append(linea_sin_sangria[8])
            tokens.append(linea_sin_sangria[9])
            tokens.append(linea_sin_sangria[10:-2])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])
            for i in range(6):
                columnas.append(str(i))
                filas.append(j) 
        if linea_sin_sangria[0:8] == palabras_reservadas[23] and linea_sin_sangria[8]==":":  #elemento
            tokens.append(palabras_reservadas[23])
            tokens.append(linea_sin_sangria[8])
            tokens.append(linea_sin_sangria[9])
            tokens.append(linea_sin_sangria[10])
            tokens.append(palabras_reservadas[24])
            tokens.append(linea_sin_sangria[15])
            tokens.append(linea_sin_sangria[16])
            tokens.append(linea_sin_sangria[17])
            nfilas = ""
            i = 18
            while linea_sin_sangria[i] != '"':
                nfilas += linea_sin_sangria[i]
                i += 1
            tokens.append(nfilas)
            tokens.append(linea_sin_sangria[i])
            tokens.append(linea_sin_sangria[i+1])
            tokens.append(linea_sin_sangria[i+2])
            tokens.append(palabras_reservadas[25])
            tokens.append(linea_sin_sangria[i+10])
            tokens.append(linea_sin_sangria[i+11])
            tokens.append(linea_sin_sangria[i+12])
            nCol = ""
            i = i+13
            while linea_sin_sangria[i] != '"':
                nCol += linea_sin_sangria[i]
                i += 1
            tokens.append(nCol)
            tokens.append(linea_sin_sangria[i])
            tokens.append(linea_sin_sangria[i+1])
            tokens.append(linea_sin_sangria[i+2])
            tokens.append(linea_sin_sangria[i+3:-3])           
            tokens.append(linea_sin_sangria[-3])
            tokens.append(linea_sin_sangria[-2])
            tokens.append(linea_sin_sangria[-1])  
            for i in range(24):
                columnas.append(str(i)) 
                filas.append(j)   
        if linea_sin_sangria[0] == '}':
            tokens.append("}")
            columnas.append(str(i)) 
            filas.append(j)
        if linea_sin_sangria[0] == "]":
            tokens.append("]")
            columnas.append(str(i)) 
            filas.append(j)
        if len(linea_sin_sangria) >= 2 and (linea_sin_sangria[0] == "," or linea_sin_sangria[1] == ","):
            tokens.append(",") 
            columnas.append(str(i))
            filas.append(j) 
        j+=1    
        i+=1 
        