
**IDEA GENERAL**
Este es un simulador de reserva de puestos en un avión. en un principio es un bosquejo de un boeing 737 nada más con 6 columnas de asientos en clase turista, 4 en clase business y 2 en primera(queda por implementar esta división).
El output serán las conexiones que existen entre los distintos asientos y la nomenclatura de cada uno (fila, columna) y las conexiones que existen con cada uno de los asientos que hay, ambos en caso de que el usuario decida verlo por escrito. Es una lista larga que resultará confusa así que recomiendo ignorar a menos que se desee lo contrario. Más adelante será necesaria para poder representar el grafo correctamente llamando a la funcion nx.draw y plt.show(). pero eso está en proceso al igual que la ponderación de los nodos y visualización en el grafo.
Por otro lado, en la línea 63 del archivo main se puede escoger de qué asiento se desea ver la puntuación pidiéndolo por fila y por columna.

**EXPLICACIÓN DEL CÓDIGO**
Este código consta de 4 módulos: seat, airplane, airplanegraph y main.
- Seat se usa para el esqueleto de los asientos (atributos y métodos de comparación)
- Airplane es para el esqueleto de avión. Define las ubicaciones de los asientos y los pasillos. Todavía no están los baños. También definen la cantidad de filas y coolumnas de cada clase. Falta mejorar esto último para implementar este elemento de manera eficiente y representar con certeza la disposición de los asientos
- Airplanegraph transformará los asientos en nodos y los ponderará según puntuación:
Los criterios para los asientos son los siguientes:
• Clase turista: 0 puntos base.
o +1 por ser de pasillo o ventana.
o +2 por proximidad a los baños (nodos especiales sin puntuación
propia).
o +3 por cercanía a la salida de emergencia.
• Clase business: 4 puntos base, con los mismos criterios adicionales de
turista.
• Primera clase: 5 puntos base, con los mismos criterios adicionales de
turista.

- Main es el principal que deberá ejecutarse para obtener la información. Por el momento por temas de facilidad el modelo de avión escogido será el boeing 737 pues solo tiene un pasillo en la mitad y es más fácil de generar, y sobretodo, de ponderar. En la línea 63 se puede modificar el asiento cuya posición respecto de la nomenclatura (row(fila), column(columna)) se desee ver.


