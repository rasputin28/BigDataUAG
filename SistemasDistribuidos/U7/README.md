Los diversos archivos con los que cuenta una computadora son en esencia datos, todo dato puede ser transferido de manera remota a otros nodos dentro de la red, por lo que es posible enviar todo tipo de archivos mediante la comunicación entre dos nodos dentro de un sistema distribuido.

En esta práctica veremos cómo convertir los datos de un archivo en mensajes para la reconstrucción del archivo en la computadora receptora de la información.

 1. Considera la revisión de los siguientes recursos interactivos "Servicios de nombrado Download Servicios de nombrado" para la realización de tu actividad. 

 https://uag.instructure.com/courses/24761/files/7837317?wrap=1

 2. Implementa 2 nodos P2P.

3. Busca en la red cómo fragmentar en paquetes un archivo.

4. Implementa el método de tu preferencia para fragmentar en paquetes el archivo en uno de los nodos (El nodo emisor).

5. Implementa el método inverso en el nodo receptor para la reconstrucción del archivo. 

Nota: Inicia con archivos pequeños, la mayoría de las veces, en casi todos los lenguajes, el manejo de archivos se dará con librerías muy independientes. El método más recomendable es un socket TCP, pero ten en mente que si el archivo es muy extenso se congelará la ventana de envío y recepción. Te recomiendo controlar la fragmentación y recibir el archivo por partes para evitar este fenómeno.

6. Sube en este espacio tu programa ejecutable y una descripción del mismo.

7. Revisa la lista de cotejo para que consideres los criterios para el desarrollo de tu entregable.