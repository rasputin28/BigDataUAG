Los sockets UDP son sockets no orientados a conexión. Esto quiere decir que un programa puede abrir un socket y ponerse a escribir mensajes en él o leer, sin necesidad de esperar a que alguien se conecte en el otro extremo del socket.

El protocolo UDP, al no ser orientado a conexión, no garantiza que el mensaje llegue a su destino. Parece claro que, si mi programa envía un mensaje y no hay nadie escuchando, ese mensaje se pierde. De todas formas, aunque haya alguien escuchando, el protocolo tampoco garantiza que el mensaje llegue. Lo único que garantiza es que, si llega, llega sin errores.

¿Para qué sirve entonces? Este tipo de sockets se suele usar para información no vital, por ejemplo, envío de gráficos a una pantalla. Si se pierde algún gráfico por el camino, veremos que la pantalla pierde un refresco, pero no es importante. El que envía los gráficos puede estar dedicado a cosas más importantes y enviar los gráficos sin preocuparse (y sin quedarse bloqueado) si el otro los recibe o no.

Otra ventaja es que, con este tipo de sockets, mi programa puede recibir mensajes de varios sitios a la vez. Si yo estoy escuchando por un socket no orientado a conexión, cualquier otro programa en otro ordenador puede enviarme un mensaje. Mi programa servidor no necesita preocuparse de establecer y mantener conexiones con varios clientes a la vez.

El concepto de cliente/servidor sigue teniendo aquí el mismo sentido. El servidor abre un socket UDP en un servicio conocido por los clientes y se queda a la escucha de este. El cliente abre un socket UDP en cualquier servicio/puerto que esté libre y envía un mensaje al servidor solicitando algo. La diferencia principal con los TCP (orientados a conexión) es que en estos últimos ambos sockets (de cliente y de servidor) están conectados y lo que escribimos en un lado, sale por el otro. En un UDP los sockets no están conectados, así que, a la hora de enviar un mensaje, hay que indicar quién es el destinatario.

Dentro de esta práctica, por favor desarrolla un socket UDP en el lenguaje de programación que sea de tu agrado y dominio. Te recomendamos que de preferencia utilices lenguajes de alto nivel, orientados a objetos como java, C# o Python, ya que se cuenta con una mayor documentación al respecto y mayor soporte.

