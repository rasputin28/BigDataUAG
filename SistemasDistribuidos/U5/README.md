En computación distribuida, la llamada a procedimiento remoto (en inglés, Remote Procedure Call, RPC) es un programa que utiliza una computadora para ejecutar código en otra máquina remota, sin tener que preocuparse por las comunicaciones entre ambas, de forma que parezca que se ejecuta en local.

Desarrollaremos una implementación de un juego del gato donde dos participantes ubicados en computadoras independientes podrán jugar el tradicional juego. Para ello el sistema debe volver transparente la comunicación entre los procesos y solo mostrará la opción seleccionada y la seleccionada por el usuario. Tengan en cuenta que el proceso debe ser síncrono ya que el juego es por turnos.

1. Considera la revisión de los siguientes recursos interactivos "RPC Llamadas a procedimientos remotos Download RPC Llamadas a procedimientos remotos" https://uag.instructure.com/courses/24761/files/7837295?wrap=1 para la realización de tu actividad.

2. Retomaremos el código P2P creado en prácticas previas.

3. Desarrolla una interfaz gráfica que nos permita visualizar un juego del gato y se implemente en el código P2P.

4. Crea un diccionario de funciones internas del gato, que nos permita simplificar la extensión de los paquetes y poder comunicar los cambios ejecutados en la interfaz.

5. Define la lógica del juego, donde permita determinar si el juego ya se ganó, se perdió o si se sigue jugando.

6. Genera el contrincante e inicia la comunicación entre procesos. 

Nota: Ten en consideración que no se puede reutilizar una casilla y no se requiere enviar paquetes complejos para definir que una casilla se ha cambiado. Puedes simplificar la complejidad definiendo que el primer programa en ejecutarse sea el jugador número uno.

7. Sube en este espacio tu programa ejecutable y una descripción del mismo.

8. Revisa la lista de cotejo para que consideres los criterios para el desarrollo de tu entregable.