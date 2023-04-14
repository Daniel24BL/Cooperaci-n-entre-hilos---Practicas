# Funcionamiento de la Programación multihilos utilizando Bucles 

# Importación de Librerias
import threading
import time

# Creación de la función
def worker():
    print('inicio')
    time.sleep(5)
    print('fin')

#worker()

# Ceación de Bucle 
threads = list()
for i in range(8) :
    t=threading.Thread(target=worker)
    threads.append(t)
    t.start()

for t in threads:
    t.join()