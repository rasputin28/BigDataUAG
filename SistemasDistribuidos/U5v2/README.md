Dentro de esta práctica desarrollaremos un juego multijugador semejante a un juego de pac-man, pero en este juego cada jugador podrá ser el cazador o la presa mediante el cambio de roles generado por algún componente predefinido y generado aleatoriamente en el sistema.

1. Considera la revisión del siguiente recurso interactivo para la realización de tu actividad.  

2. Retomaremos el código P2P creado en prácticas previas. Puedes crear un esquema centralizado si te simplifica la práctica. 

3. Construye una cuadrícula como interfaz de 20x20 donde cada cuadro puede aparecer un pacman específico.

4. Crea un diccionario de funciones internas del juego, que nos permita simplificar la extensión de los paquetes y poder comunicar los cambios ejecutados en la interfaz. Los movimientos son: Moverse arriba, abajo, izquierda, derecha. Debemos agregar aleatoriamente una moneda que permita a un jugador convertirse en casado y pueda comerse a los otros pacmans. Se comerá a un pacman cuando ambos estén en la misma casilla.

5. Define la lógica del juego, donde permita determinar si el juego ya se ganó, se perdió o si se sigue jugando. El juego terminará cuando sólo quede un pacman en la escena. 

6. El número mínimo de jugadores será 4. 

Nota: Ten en cuenta que cada nuevo cliente será un jugador asignado a la escena, esto lo puedes predefinir o volver aleatorio. Recuerda que el objetivo es que un solo sistema pueda replicarse y ser capaz de adaptarse a nuevos nodos.

7. Sube en este espacio tu programa ejecutable y una descripción del mismo.

8. Revisa la lista de cotejo para que consideres los criterios para el desarrollo de tu entregable.