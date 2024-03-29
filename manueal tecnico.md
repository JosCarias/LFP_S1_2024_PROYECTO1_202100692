# Manual de Tecnico de la proyecto 1

## Introducción
El proyecto consiste en realizar un editor web simple el cual generará código HTML, la sintaxis
que se usará en el editor se explica más adelante. Se debe poder modificar desde el editor el
código que se cargara para generar código HTML.

## Requisitos del Sistema
- Visual code
- Sistema Operativo: Compatible con Pytho
- Python 3.12.2  o superior
- Graphviz
- Navegador Web: Google Chrome, Mozilla Firefox, Safari

## Clase principal
Esta clase actúa como punto de entrada del programa. Se encarga de iniciar la aplicación y dirigir el flujo de ejecución hacia las otras clases y componentes del sistema. En el diagrama mostrado se resalta que esta clase es la principal y que no cuenta con un constructor explícito, lo que indica que su inicialización y ejecución se realizan directamente al iniciar el programa.
![alt text](Imagenes\7.png)

## Clase analisis lexico
El propósito de esta clase es llevar a cabo el análisis léxico del código fuente proporcionado por el usuario. Utiliza un diccionario de palabras reservadas para identificar y clasificar tokens específicos en el código. La función analizador lee línea por línea del archivo, buscando coincidencias con las palabras reservadas definidas en el diccionario. Cuando encuentra una coincidencia, registra la fila y la columna correspondientes en las que se encontró la palabra clave.
![alt text](Imagenes\9.png)
aqui tenemos definido un diccionario con palabras reservadas
![alt text](Imagenes\10.png)
esta funcion se encargar de analizar el archivo y leerlo busca la palabras definidas en el diccionario y cuando se encuentra la concidencia y agrega la fila y la columna
![alt text](Imagenes\11.png)

## Clase automata finito determinista(hacerHtml.py)
Esta clase se encarga de implementar un autómata finito determinista (DFA) utilizando la librería Graphviz. El propósito del DFA es representar y visualizar el proceso de análisis léxico en forma de un diagrama de estados. El diagrama generado se guarda como un archivo PDF para su posterior visualización y referencia.
![alt text](Imagenes\13.png)

## Clase hacer html
La responsabilidad de esta clase es generar la estructura básica de un documento HTML a partir de los datos recopilados durante el análisis léxico y otros procesos del sistema. Se encarga de crear el esqueleto HTML necesario, incluyendo las etiquetas principales como <html>, <head> y <body>, así como otras etiquetas necesarias según sea el caso. Además, se encarga de escribir el contenido analizado en el documento HTML resultante y de guardarlo en un archivo para su posterior uso o visualización.
![alt text](Imagenes\14.png)

## Clase (reporte.py)
Esta clase se encarga de generar una tabla que muestra el resultado del análisis léxico. Utiliza los datos recopilados durante el análisis, como los tokens identificados, las filas y columnas correspondientes, y los presenta de manera organizada en una tabla HTML. Esta tabla proporciona una visualización clara y estructurada de la información analizada, lo que facilita su comprensión y referencia por parte del usuario.
![alt text](Imagenes\15.png)

## Clase intefaz(interfaz.py)
La clase interfaz en reporte.py se encarga de crear la interfaz gráfica del programa utilizando la biblioteca Tkinter de Python. La interfaz gráfica proporciona una manera fácil e intuitiva para que los usuarios interactúen con el sistema y visualicen los resultados del análisis léxico.

Componentes de la interfaz
Botón "Cargar Archivo": Permite al usuario seleccionar y cargar un archivo de código fuente para su análisis.
Área de texto "Editor": Muestra el contenido del archivo cargado y permite al usuario realizar modificaciones si es necesario.
Botón "Analizar": Inicia el proceso de análisis léxico del código fuente cargado.
Área de texto "Resultados": Muestra los resultados del análisis léxico, como los tokens identificados y sus ubicaciones en el código fuente.
Botón "Generar HTML": Genera un archivo HTML que muestra los resultados del análisis léxico en forma de una tabla estructurada.
Botón "Limpiar": Borra el contenido de las áreas de texto "Editor" y "Resultados", permitiendo al usuario cargar y analizar un nuevo archivo si lo desea.
Botón "Salir": Cierra la aplicación.
Funcionalidad
El botón "Cargar Archivo" permite al usuario seleccionar un archivo de código fuente desde el sistema de archivos local y cargarlo en el área de texto "Editor".
Al hacer clic en el botón "Analizar", se inicia el proceso de análisis léxico del código fuente cargado, y los resultados se muestran en el área de texto "Resultados".
El botón "Generar HTML" genera un archivo HTML que presenta los resultados del análisis léxico en forma de una tabla estructurada.
El botón "Limpiar" borra el contenido del área de texto "Editor" y "Resultados", permitiendo al usuario cargar y analizar un nuevo archivo.
El botón "Salir" cierra la aplicación.
![alt text](Imagenes\16.png)







