import networkx as nx

class AirplaneGraph:
    def __init__(self):
        self.graph = nx.Graph() 
    
    def add_seat(self, seat):
        """Añade un asiento como nodo al grafo."""
        self.graph.add_node((seat.row, seat.column), seat=seat)
    
    def add_edge(self, seat1, seat2):
        """Conecta asientos adyacentes en el grafo."""
        distance = abs(seat1.row - seat2.row) + abs(seat1.column - seat2.column)
        self.graph.add_edge((seat1.row, seat1.column), (seat2.row, seat2.column), weight=distance)
    
    def find_seat_by_position(self, row, column):
        """Encuentra un asiento en el grafo por fila y columna."""
        return self.graph.nodes.get((row, column), {}).get("seat", None)
    
    def calculate_seat_score(self, seat):
        """Calcula la puntuación de un asiento basada en su clase, posición, y cercanía a la salida."""
        score = 0
        score += 5 if seat.class_type == "first_class" else 3 if seat.class_type == "business_class" else 1
        score += 2 if seat.position == "window" else 1 if seat.position == "aisle" else 0
        score += max(0, 10 - seat.distance_to_exit)  # Puntuación adicional para cercanía a la salida
        return score
