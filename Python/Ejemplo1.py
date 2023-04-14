# Funcionamiento de la Programación multihilos sin sincronización

# Importación de Librerias
import threading
from time import sleep
import random

# Creación de la función
def ejecutar():
    print(f'Comienza {threading.current_thread().name}')
    sleep(random.random())  # esperamos un tiempo aleatorio entre 0 y 1 segundos
    print(f'Termina {threading.current_thread().name}')


# creamos los hilos
hilo1 = threading.Thread(target=ejecutar, name='Hilo 1')
hilo2 = threading.Thread(target=ejecutar, name='Hilo 2')

# ejecutamos los hilos
hilo1.start()
hilo2.start()

print('El hilo principal no espera por el resto de hilos para finalizar.')
