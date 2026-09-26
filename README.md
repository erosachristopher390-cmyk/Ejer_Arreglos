# Ejer_Arreglos

Lo que realiza el programa es generar una tabla bidimensional en la que las filas representan los 12 meses del año y las columnas representan los departamentos de la tienda.

Inicialmente, el programa cuenta con tres departamentos:

Ropa
Deportes
Juguetería

El programa permite agregar nuevos departamentos, registrar ventas manualmente, buscar una venta específica, eliminar una venta, mostrar todas las ventas y generar ventas aleatorias.

El programa cuenta con 7 funciones principales. Sin embargo, solamente 6 corresponden directamente a las opciones principales del menú, ya que mostrar_meses() y mostrar_departamentos() son funciones auxiliares utilizadas para facilitar la selección de datos.

Funciones del programa

generar_ventas()

Genera automáticamente valores aleatorios para las ventas de cada departamento durante los 12 meses. De esta manera, la tabla puede comenzar con datos sin necesidad de introducir todas las ventas manualmente.

agregar_departamento()

Permite agregar un nuevo departamento al programa. Al agregarlo, se crea automáticamente una nueva columna en el arreglo bidimensional y se generan ventas aleatorias para ese departamento en los 12 meses.

insertar_venta(mes, departamento, cantidad)

Permite introducir o modificar manualmente una venta. Recibe el mes, el departamento y la cantidad de la venta, y almacena esa información en la posición correspondiente del arreglo.

buscar_venta(mes, departamento)

Permite consultar una venta específica indicando el mes y el departamento. El programa muestra la cantidad de venta almacenada en esa posición.

eliminar_venta(mes, departamento)

Permite eliminar una venta específica. Para hacerlo, cambia el valor almacenado en esa posición del arreglo a 0.

mostrar_ventas()

Muestra en forma de tabla todas las ventas registradas, organizadas por meses y departamentos.

mostrar_meses()

Muestra una lista numerada de los 12 meses para que el usuario pueda seleccionar fácilmente el mes que desea utilizar en las diferentes operaciones.

mostrar_departamentos()

Muestra una lista numerada de los departamentos existentes para que el usuario pueda seleccionar el departamento con el que desea trabajar.

Menú del programa

Al ejecutar el programa se muestran las siguientes opciones:

Insertar venta
Buscar venta
Eliminar venta
Mostrar todas las ventas
Agregar departamento
Regenerar ventas aleatorias
Salir

De esta manera, el programa permite administrar las ventas de diferentes departamentos y meses utilizando un arreglo bidimensional dinámico, ya que es posible agregar nuevas columnas para los departamentos conforme sea necesario.
