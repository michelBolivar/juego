Juego --  Space Defender

Elaborado por -- Laura Michel Bolivar Rincon

Sinopsis:
En este juego en desarrollo, te sumergirás en la experiencia de controlar una nave espacial mientras navegas por el vasto espacio. Sin embargo, tu travesía estará plagada de peligros, ya que una serie de meteoritos se interpondrán en tu camino, amenazando con destruir tu nave.

Tu objetivo principal será destruir estos meteoritos utilizando un rayo láser. Cada impacto exitoso te otorgará puntos, lo que te permitirá avanzar en el juego.Sin embargo, ten en cuenta que tu nave tiene una capacidad limitada para resistir los impactos. Si una cantidad determinada de meteoritos colisiona con tu nave, el juego llegará a su fin. 


*Descripcion*

Para el desarrollo del juego, se utilizó el lenguaje de programación Python y se hizo uso de la biblioteca Pygame.

En el código, se ha documentado la funcionalidad de cada clase y método empleado. Sin embargo, a continuación se proporcionará una breve descripción de los mismos

 --> Player: representa al jugador en el juego y define su comportamiento y características. Esta clase contiene el método 'Shoot', el cual permite al jugador disparar el láser. El método 'Shoot' se activa cuando el jugador presiona la barra espaciadora y realiza las acciones necesarias para disparar el láser en la dirección adecuada.
 
-->Meteor: esta clase representa un meteorito en el juego y se encarga de su posicionamiento y movimiento en la pantalla.

 --> Bullet: esta clase representa una bala disparada por la nave espacial y se encarga de su posicionamiento y movimiento en la pantalla. Si la bala sale de la pantalla, se elimina del juego para liberar recursos.
 
--> Explosion: esta clase representa una explosión en el juego y se encarga de animarla mediante una serie de cuadros. La explosión se actualiza en cada fotograma, mostrando el siguiente cuadro de la animación según la velocidad establecida. Cuando se completa la animación, la explosión se elimina del juego.


Asimismo, se han incluido imágenes, sonidos y animaciones que se encuentran en la carpeta 'assets', adjunta al código.