from airplane import Airplane
from airplanegraph import AirplaneGraph
import networkx as nx
import matplotlib.pyplot as plt

def main():
    # Configuración del avión 
    model = "Boeing 737"
    total_seats = 150
    first_class_rows = 3
    business_class_rows = 5
    economy_class_rows = 15
    
    # Crear instancia del avión y generar los asientos
    airplane = Airplane(model, total_seats, first_class_rows, business_class_rows, economy_class_rows)
    print(f"Avión {model} con {total_seats} asientos generado.")
    
    # Crear el grafo para modelar la disposición de los asientos
    airplane_graph = AirplaneGraph()
    
    # Añadir asientos al grafo
    for seat_key, seat in airplane.seats.items():
        airplane_graph.add_seat(seat)

    # Conectar asientos adyacentes en el grafo
    for row in range(1, first_class_rows + business_class_rows + economy_class_rows + 1):
        for col in range(1, 7):  # Suponiendo 6 columnas (A, B, C, D, E, F)
            seat = airplane.get_seat(row, col)
            if seat:
                # Conectar con asiento a la derecha
                right_seat = airplane.get_seat(row, col + 1)
                if right_seat:
                    airplane_graph.add_edge(seat, right_seat)
                
                # Conectar con asiento en la fila de adelante
                if row < first_class_rows + business_class_rows + economy_class_rows:
                    front_seat = airplane.get_seat(row + 1, col)
                    if front_seat:
                        airplane_graph.add_edge(seat, front_seat)

    # Mostrar el grafo
    print("Grafo de asientos creado:")
    eleccion1 = input("¿Desea ver los nodos? (s/n): ")
    if eleccion1.lower() == "s":
        print(f"Nodos (asientos): {airplane_graph.graph.nodes}")
    else:
        print("Nodos no mostrados.")
    eleccion2 = input("¿Desea ver las aristas? (s/n): ")
    if eleccion2.lower() == "s":
        print(f"Aristas (conexiones entre asientos): {airplane_graph.graph.edges}")
    else:
        print("Aristas no mostradas.")

    # Mostrar el grafo en una ventana
    eleccion3 = input("¿Desea visualizar el grafo? (s/n): ")
    if eleccion3.lower() == "s":
        nx.draw(airplane_graph.graph, with_labels=True)
        plt.show()
    else:
        print("Grafo no visualizado.")
    
    # Ejemplo de búsqueda de asiento y cálculo de puntuación
    row, column = 1, 1  # Cambiar para probar diferentes asientos
    seat = airplane_graph.find_seat_by_position(row, column)
    if seat:
        score = airplane_graph.calculate_seat_score(seat)
        print(f"Asiento en fila {row}, columna {column} tiene una puntuación de {score}.")
    else:
        print(f"Asiento en fila {row}, columna {column} no encontrado.")

if __name__ == "__main__":
    main()
