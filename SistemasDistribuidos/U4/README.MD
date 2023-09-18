Podemos definir “Comunicación indirecta” como la comunicación entre entidades en un sistema distribuido a través de un intermediario, sin un acoplamiento directo entre el remitente y el receptor o receptores. Existen 4 modelos de comunicación:

- Comunicación de grupo: ofrece un servicio a través del cual un mensaje es enviado a un grupo y este es entregado a todos los miembros del mismo.
- Publicador/suscriptor: es un sistema en el que los publicadores colocan eventos estructurados en un servicio de eventos y los suscriptores expresan interés en eventos particulares a través de suscripciones.
- Colas de mensajes: en contraposición con los grupos o los sistemas de publicador/suscriptor que proporcionan un estilo de comunicación uno-a-muchos, las colas de mensajes proporcionan un servicio punto-a-punto usando colas de mensajes como sistema de indirección.
- Sistemas de memoria compartida: es un sistema de comunicación indirecta mediante la escritura o lectura de tuplas en sistemas de memoria compartida.

Además de las breves definiciones anteriores podemos indicar las siguientes diferencias entre los diferentes modelos:

- En comunicación de grupo, el grupo está bien definido y gestionado. Soporta orden de entrega en los mensajes y garantiza la entrega además de ser tolerante a fallos.
- En el modelo publicador/suscriptor los eventos son publicados sin conocer si existe interés en ellos. Los suscriptores pueden contactar con los publicadores si tienen interés, lo que puede provocar sobrecarga en un publicador.
- Las colas de mensajes soportan únicamente comunicaciones punto-a-punto, mientras que los otros modelos ofrecen un estilo uno-a-muchos. En el caso de memoria compartida soporta punto-a-punto, uno-a-muchos y muchos-a-muchos.
- Las colas de mensajes son más estructuradas y fiables que los sistemas publicador/suscriptor.
- La memoria compartida es la manera más simple de comunicación entre procesos y suele usarse en clústeres en donde todos los nodos son iguales y utilizan un mismo sistema operativo.
- Los grupos y memoria compartida tienen una escalabilidad limitada, mientras que los otros modelos tienen posibilidades de escalado mayores.

Dentro de esta práctica retomaremos la idea de un chat, pero esta vez no utilizaremos el esquema punto a punto, centralizaremos la información y se distribuirá a cada nodo que se encuentre activo dentro del sistema distribuido bajo el esquema publicación-suscripción.

1. Considera la revisión del siguiente recurso interactivo para la realización de tu actividad.

2. Desarrolla un servidor que permita el registro de una cantidad indefinida de nodos P2P. Esto se puede hacer creando una base de datos interna en memoria RAM con vectores de strings que almacene las IP´s y los Puertos por donde escucharán los nodos clientes.

3. Recupera la práctica 3, pero modifiquemos el nodo creado predefiniendo solamente como nodo de envío al nodo servidor que previamente hemos creado.

4. El nodo Servidor debe de enviar los paquetes recibidos a todos los nodos que previamente se hayan dado de alta en él.

5. Replica varias veces el nodo cliente para visualizar el envío y recepción de paquetes. 

Nota: Ten en cuenta que el nodo servidor formará un esquema de estrella centralizado. Es necesario predefinir por cuál puerto los nodos clientes escucharán, para que sea enviada dicha información como paquete principal y se almacene este listado en el servidor. 

6. Sube en este espacio tu programa ejecutable y una descripción del mismo.

7. Revisa la lista de cotejo para que consideres los criterios para el desarrollo de tu entregable.