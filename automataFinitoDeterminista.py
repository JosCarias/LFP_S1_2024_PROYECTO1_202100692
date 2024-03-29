from graphviz import Digraph

def Grafica():
    # Crear el gráfico
    dot = Digraph()

    # Definir los estados
    estados = ['A','B','C','D']

    # Definir el estado inicial y los estados de aceptación
    estado_inicial = 'A'
    estados_aceptacion = ['B', 'C']

    cadena = '''Transiciones:
            A -> aB 
            A -> bC
            A -> dD
            B -> aB
            D -> cD
            D -> dC
            B -> ε
            C -> ε'''

    dot.node(cadena, shape='box')
    

    # Añadir los estados al gráfico
    for estado in estados:
        if estado == estado_inicial:
            dot.edge("Inicio",estado)
            dot.node(estado, shape='circle')
        elif estado in estados_aceptacion:
            dot.node(estado, shape='doublecircle')
        else:
            dot.node(estado)

    # Añadir las transiciones
    transiciones = {
        ('A', 'a'): 'B',
        ('A', 'b'): 'C',
        ('A', 'd'): 'D',
        ('B', 'a'): 'B',
        ('D', 'c'): 'D',
        ('D', 'd'): 'C'
    }

    for transicion, destino in transiciones.items():
        dot.edge(transicion[0], destino, label=transicion[1])
        
    cadena = '''Definiciones:
            A -> Letras del alfabeto mayúsculas y minúsculas 
            B -> Los simbolos: , [ ] { } 
            C -> cadena de caracteres, acepta cualquier cosas menos los saltos de lineas
            D -> Comillas dobles'''

    dot.node(cadena, shape='box')

    # Guardar y mostrar el gráfico
    dot.render('grafica')
    dot.view()
    
