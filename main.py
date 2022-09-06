from arbol import Arbol

arbol = Arbol(dato_raiz='Antioquia', heuristica_raiz=366)

arbol.agregar_nodo(dato='Santander', heuristica=329, coste=118)
arbol.agregar_nodo(dato='Boyaca', heuristica=253, coste=140)
arbol.agregar_nodo(dato='Cundinamarca', heuristica=374, coste=75)
arbol.agregar_nodo(dato='Caldas', heuristica=374, coste=75)

arbol.agregar_nodo(dato_padre='Santander', dato='Boyaca',
                   heuristica=190, coste=225)

arbol.agregar_nodo(dato_padre='Boyaca', dato='Casanare',
                   heuristica=150, coste=195)
arbol.agregar_nodo(dato_padre='Boyaca', dato='Meta',
                   heuristica=90, coste=200)

arbol.agregar_nodo(dato_padre='Casanare', dato='Vichada',
                   heuristica=70, coste=155)

arbol.agregar_nodo(dato_padre='Vichada', dato='Guaviare',
                   heuristica=50, coste=75)

arbol.agregar_nodo(dato_padre='Meta', dato='Guaviare',
                   heuristica=50, coste=40)

arbol.agregar_nodo(dato_padre='Guaviare', dato='Vaupes',
                   heuristica=20, coste=29)
arbol.agregar_nodo(dato_padre='Guaviare', dato='Caqueta',
                   heuristica=30, coste=55)

arbol.agregar_nodo(dato_padre='Caqueta', dato='Amazonas',
                   heuristica=0, coste=35)

arbol.agregar_nodo(dato_padre='Vaupes', dato='Amazonas',
                   heuristica=0, coste=25)

arbol.agregar_nodo(dato_padre='Cundinamarca', dato='Meta',
                   heuristica=90, coste=180)
arbol.agregar_nodo(dato_padre='Cundinamarca', dato='Tolima',
                   heuristica=60, coste=135)

arbol.agregar_nodo(dato_padre='Tolima', dato='Huila',
                   heuristica=40, coste=65)

arbol.agregar_nodo(dato_padre='Huila', dato='Caqueta',
                   heuristica=30, coste=45)

arbol.agregar_nodo(dato_padre='Caldas', dato='Risaralda',
                   heuristica=120, coste=80)

arbol.agregar_nodo(dato_padre='Risaralda', dato='Quindio',
                   heuristica=110, coste=20)

arbol.agregar_nodo(dato_padre='Quindio', dato='Tolima',
                   heuristica=60, coste=40)

print('Búsquedas')
print('\nBúsqueda por profundidad')
arbol.busqueda_profundidad()
print('\n\nBúsqueda por amplitud')
arbol.busqueda_amplitud()
print('\n\nBúsqueda de primero el mejor RECURSIVO')
arbol.busqueda_primero_mejor_recursiva()