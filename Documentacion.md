##Reporte: "El problema de los filósofos comensales".
####Integrantes del equipo:
Oswaldo Cordoba Jimenez  201627085.
Cesar Ruiz Rodrigues Flores  201624846.
Oscar Arzeta Rodriguez  201629369.

####Introduccion.
El **Porblema de los filósofos** es un problema tipico en las ciencias de la computacion, ya que este representa el problema de la sincronización de procesos en un sistema operativo. Cinco filósofos se sientan alrededor de una mesa y pasan su vida cenando y pensando, cada filośofo tiene un plato de spaguetti y un tenedor a la izquierda y uno a la derecha. Para poder comer, tiene que tomar ambos tenedores y cada filósofo sólo puede tomar los que estan a su izquierda y derecha. Si cualquier filósofo toma un tenedor y el otro está ocupado, se quedará esperando, con el tenedor en la mano, hasta que pueda tomar el otro tenedor, para luego empezar a comer.

Si dos filósofos adyacentes intentan tomar el mismo tenedor a una vez, se produce una condición de carrera: ambos compiten por tomar el mismo tenedor, y uno de ellos se queda sin comer.

Si todos los filósofos toman el tenedor que está a su derecha al mismo tiempo, entonces todos se quedarán esperando eternamente, porque alguien debe liberar el tenedor que les falta. Nadie lo hará porque todos se encuentran en la misma situación (esperando que alguno deje sus tenedores). Entonces los filósofos se morirán de hambre. Este bloqueo mutuo se denomina interbloqueo o deadlock.

El problema consiste en encontrar un algoritmo que permita que los filósofos nunca se mueran de hambre.

####Codigo (Python).
Para poder modelar este problema y su solución usaremos hilos(Threads) para simular a los filósofos y los tenedores seran los recursos compartidos, seran la zona critica en el programa, ya que 2 filósofos no pueden usar el mismo tenedor al mismo tiempo, y a su vez deben liberarlos para que otro pueda usarlo.
Para emprezar, importaremos las siguientes bibliotecas:
```
import threading
import random
import time
```
Des pues creamos la clase "Filosofos" y en su constructor declaramos su nombre, estado, tenedor derecho y tenedor izquierdo.
```
class Filosofos(threading.Thread):

    def __init__(self, name, state,  leftfork, rightfork):
        threading.Thread.__init__(self)
        self.leftfork = leftfork
        self.rightfork = rightfork
        self.name = name
        self.state = state
```