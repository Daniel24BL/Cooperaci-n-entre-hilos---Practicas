# Funcionamiento de la Programación multihilos teniendo varios procesos en una lista 

# Importación de Librerias
import threading
import time

# Creación de la función 1 (Simulación de la tarea con un solo hilo)
def worker_1 (rango):      
    lista = list()
    for i in range(rango):      # El ciclo nos devuelve el rango que le pasemos como parámetro
        lista.append(i)         # Se añade la lista en este caso en el evento "i"
        time.sleep(0.01)        # Implementación del tiempo de ejecución 
    return lista

# Indicamos los parámetros y el número de interacciones que tendrá la lista 
# Nos indicara el tiempo en que tardo en ejecutarse la tarea
t0 = time.time()
lista= worker_1(100)
tf= time.time()-t0
print('Tiempo total en 1 thread: {} \n'.format(tf))
print(lista, '\n')



# Creamos una nueva lista
# Indicación del número de hilos con los que se desea trabajar
n_threads = 4
lista_2 = list()

# Creación de la función 2 (Simulación de la tarea con varios hilos)
def worker(inicio, fin):      # parametros por separado  
    for i in range (inicio, fin):
        lista_2.append(i)
        time.sleep(0.01)
    return lista_2

# Arreglos para la lista 2
p= len(lista)//n_threads
inicios = list()
fines = list()
inicio = 0
fin = p

# Bucle para que cada interacción funcione como un hilo
for i in range(n_threads):
    inicios.append(inicio)
    fines.append(fin)
    inicio += p
    fin += p

# Se crea una especie de contador para calcular el tiempo en que demora en ejecutar la tarea 
t0 = time.time()
threads = list()
for i in range(len(inicios)):
    t = threading.Thread(target=worker,args=(inicios[i], fines[i],))
    threads.append(t)
    t.start()


# Sincronización 
for t in threads:
    t.join()

#lista_2.sort()   #  El método sort() nos permite ordenar una lista en orden ascendente o descendente
tf = time.time() - t0
print('Tiempo total en {} threads: {} segundos \n'.format(n_threads, tf))
print(lista_2)
