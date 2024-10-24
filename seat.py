class Seat:
    def __init__(self, seat_number, class_type, position, comfort_level, distance_to_exit, status, row, column):
        self.seat_number = seat_number
        self.class_type = class_type
        self.position = position
        self.comfort_level = comfort_level
        self.distance_to_exit = distance_to_exit
        self.status = status
        self.row = row
        self.column = column

        #Métodos para obtener los atributos de la clase (getters)
    def get_seat_number(self):
        return self.seat_number
    
    def get_class_type(self):
        return self.class_type
    
    def get_position(self):
        return self.position
    
    def get_comfort_level(self):
        return self.comfort_level
    
    def get_distance_to_exit(self):
        return self.distance_to_exit
    
    def get_status(self):
        return self.status
    
    def get_row(self):
        return self.row
    
    def get_column(self):
        return self.column
    
    def set_seat_number(self, seat_number):
        self.seat_number = seat_number

    def set_class_type(self, class_type):
        self.class_type = class_type
    
    def set_position(self, position):
        self.position = position
    
    def set_row(self, row):
        self.row = row
    
    def set_column(self, column):
        self.column = column   
    
    #Método para comparación

    def __lt__(self, other):
        # comparar por clase (asientos de mayor clase son más preferidos)
        if self.class_type != other.class_type:
            return self.class_type < other.class_type
        # Comparar por comodidad (asientos más cómodos son más preferidos)
        if self.comfort_level != other.comfort_level:
            return self.comfort_level < other.comfort_level
        # Comparar por distancia a la salida
        return self.distance_to_exit < other.distance_to_exit

    def __gt__(self,other):
        # Misma lógica que el método __lt__ pero al revés
        if self.class_type != other.class_type:
            return self.class_type > other.class_type
        if self.comfort_level != other.comfort_level:  
            return self.comfort_level > other.comfort_level
        return self.distance_to_exit > other.distance_to_exit
    