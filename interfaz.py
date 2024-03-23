import tkinter as tk
from tkinter import filedialog
from analisisLexico import cargar_archivo_txt

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
        ruta_archivo = filedialog.askopenfilename()
        if ruta_archivo:
            # Leer el contenido del archivo
            with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
                contenido = archivo.read()
            # Insertar el contenido en el cuadro de texto
            textbox.delete(1.0, tk.END)  # Limpiar el contenido actual
            textbox.insert(tk.END, contenido)
    
    # Botón cargar
    boton = tk.Button(ventana, text="CargarArchivo", command=abrir_explorador,font=tamaño_fuente)
    boton.grid(column=0,row=1,pady=5,padx=5)
    
    # Botón traducir
    boton = tk.Button(ventana, text="Traducir", command="",font=tamaño_fuente)
    boton.grid(column=1,row=1,pady=5,padx=5)
    
    # Crear el cuadro de texto
    textbox = tk.Text(ventana, height=30, width=40,font=tamaño_fuente)
    textbox.grid(column=1,row=2,pady=5,padx=5)
    
    # Crear el cuadro de texto
    textbox = tk.Text(ventana, height=30, width=40,font=tamaño_fuente)
    textbox.grid(column=0,row=2,pady=5,padx=5)
    
    # Botón en la ventana
    boton = tk.Button(ventana, text="Cerrar Ventana", command=ventana.destroy,font=tamaño_fuente)
    boton.grid(column=1,row=5,pady=5,padx=5)
    
    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()