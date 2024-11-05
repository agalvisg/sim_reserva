from seat import Seat

class Airplane: 
    
    def __init__(self, model, total_seats, first_class_rows, business_class_rows, economy_class_rows):
        self.model = model
        self.total_seats = total_seats
        self.first_class_rows = first_class_rows
        self.business_class_rows = business_class_rows
        self.economy_class_rows = economy_class_rows
        self.seats = {}  # Diccionario para almacenar asientos por fila y columna
        self.generate_seats()  # Generar los asientos al inicializar la instancia
    
    def get_total_seats(self):
        return self.total_seats
    
    def generate_seats(self):
        """Genera asientos para el avión según la configuración dada de filas y columnas."""
        row_number = 1
        
        # Generar primera clase
        for _ in range(self.first_class_rows):
            self._add_row(row_number, "first_class")
            row_number += 1
        
        # Generar business class
        for _ in range(self.business_class_rows):
            self._add_row(row_number, "business_class")
            row_number += 1
            
        # Generar clase turista
        for _ in range(self.economy_class_rows):
            self._add_row(row_number, "economy_class")
            row_number += 1
            
    def _add_row(self, row_number, class_type):
        """Helper que agrega una fila completa de asientos con el tipo de clase especificado."""
        num_columns = 6  # Ejemplo de 6 columnas (A, B, C, D, E, F)
        for col in range(1, num_columns + 1):
            # Asignar posición según la columna (A, F = ventana, B, E = pasillo, etc.)
            position = "window" if col in [1, num_columns] else "aisle" if col in [2, num_columns - 1] else "middle"
            
            # Configurar nivel de comodidad y distancia
            comfort_level = 1 if class_type == "first_class" else 2 if class_type == "business_class" else 3
            distance_to_exit = row_number  # Distancia simplificada para el ejemplo
            
            # Crear asiento
            seat = Seat(
                seat_number=row_number * 10 + col,  # Número único por fila y columna
                class_type=class_type,
                position=position,
                comfort_level=comfort_level,
                distance_to_exit=distance_to_exit,
                status="available",
                row=row_number,
                column=col
            )
            
            # Almacenar asiento en el diccionario
            self.seats[(row_number, col)] = seat
    
    def get_seat(self, row, column):
        """Devuelve el asiento especificado por la fila y columna, o None si no existe."""
        return self.seats.get((row, column), None)
