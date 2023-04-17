# Funcionamiento de la Programación multihilos con sincronización
# llamada al método join()

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

# esperamos a que terminen los hilos
# El método join () se utiliza para especificar los elementos de una secuencia de caracteres
hilo1.join()
hilo2.join()

print('El hilo principal sí espera por el resto de hilos para finalzar.')