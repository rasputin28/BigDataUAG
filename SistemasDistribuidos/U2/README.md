El protocolo TCP es un protocolo de la capa de transporte que es orientado a conexión, esto significa que antes de intercambiar los datos reales hay un paso previo para establecer una comunicación. Este protocolo también garantiza que toda la transmisión de los datos se hace sin errores, el propio TCP se encarga de reenviar los datos nuevamente en caso de que el receptor no los reciba a tiempo o los reciba dañados, además, garantiza también el orden, por lo que nos aseguramos de que los procesos van a recibir todos los datos en orden desde su origen.

¿Cuáles son las ventajas del Socket TCP?
-    Cuando se envía un paquete, el receptor confirma que se le entregó el paquete.
-    Si se pierde un paquete, éste lo reenvía.
-    Como los segmentos están numerados, estos llegan en el mismo orden con el que fueron enviados.
-    Si hay congestión, retrasa los demás paquetes para evitar la pérdida de paquetes.

Entre las desventajas podemos encontrar su dificultad para diferenciar interfaces, su lentitud en redes con poco tráfico o su escaso rendimiento a la hora de trabajar con servidores de ficheros o de impresión.

Dentro de esta práctica por favor desarrolla un socket TCP en el lenguaje de programación que sea de tu agrado y dominio. Te recomendamos que de preferencia utilices lenguajes de alto nivel orientados a objetos como java, C# o Python, ya que se cuenta con una mayor documentación al respecto y mayor soporte.# 
