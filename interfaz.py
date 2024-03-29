import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from analisisLexico import analizador, cargar_archivo_txt
from reporte import reporte
from hacerHtml import hacerHtml
from automataFinitoDeterminista import Grafica


ruta=""

def interfaz():
    # Crear la ventana
    ventana = tk.Tk()
    ventana.title("Proyecto 1 LFP")
    ventana.geometry("750x720")  # Tamaño de la ventana (ancho x alto)
    
    #tamaño de fuente
    tamaño_fuente = ("Arial", 12) 
    
    # Crear un frame
    frame = tk.Frame(ventana, width=1185,height=50, background="grey",relief=tk.SUNKEN)
    frame.grid(column=0,columnspan=3, row=0, pady=5, padx=5)
    
    # Crear una etiqueta
    etiqueta = tk.Label(frame ,text="Proyecto 1 LFP, Nombre: Josue Ricardo Carias Ordoñez, Carnet: 202100692",font=tamaño_fuente, background="grey")
    etiqueta.grid(padx=10, pady=10)
    
    # Función para abrir el explorador de archivos y obtener la ruta del archivo seleccionado
    def abrir_explorador():
        global ruta
        ruta = filedialog.askopenfilename()
        
        if ruta:
            # Leer el contenido del archivo
            with open(ruta, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            # Insertar el contenido en el cuadro de texto
            textboxIz.delete(1.0, tk.END)  # Limpiar el contenido actual
            textboxIz.insert(tk.END, contenido)
        messagebox.showinfo("Mensaje", "Se desplegado el archivo")
    
    # Botón cargar
    boton = tk.Button(ventana, text="CargarArchivo", command=abrir_explorador,font=tamaño_fuente)
    boton.grid(column=0,row=1,pady=5,padx=5)
    
    #funcion para cargar 
    def leerArchivo():
        global ruta
        contenido = cargar_archivo_txt(ruta)
        analizador(contenido)  # Lee desde la primera línea hasta el último caracter
        messagebox.showinfo("Mensaje", "Se ha cargado el archivo")
        hacerHtml()
        with open("LFP_S1_2024_PROYECTO1_202100692/resultado.html", 'r', encoding='utf-8') as archivo:
            contenido = archivo.read()
        textboxDe.delete(1.0, tk.END)  # Limpiar el contenido actual
        textboxDe.insert(tk.END, contenido)
        
    
    # Botón traducir
    boton = tk.Button(ventana, text="Traducir", command=leerArchivo,font=tamaño_fuente)
    boton.grid(column=1,row=1,pady=5,padx=5)
    
    # Crear el cuadro de texto
    textboxIz = tk.Text(ventana, height=30, width=40,font=tamaño_fuente)
    textboxIz.grid(column=0,row=2,pady=5,padx=5)
    
    # Crear el cuadro de texto
    textboxDe = tk.Text(ventana, height=30, width=40,font=tamaño_fuente)
    textboxDe.grid(column=1,row=2,pady=5,padx=5)
    
    def reporteDeArchivo():
        reporte()
        Grafica()
    
    # Botón en la reporte
    boton = tk.Button(ventana, text="Reporte", command=reporteDeArchivo,font=tamaño_fuente)
    boton.grid(column=0,row=5,pady=5,padx=5)
    
    # Botón en la ventana
    boton = tk.Button(ventana, text="Cerrar Ventana", command=ventana.destroy,font=tamaño_fuente)
    boton.grid(column=1,row=5,pady=5,padx=5)
    
    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()