import threading
import time

# Functie voor de eerste thread
def print_numbers():
    for i in range(1, 6):
        print("Thread 1: ", i)
        time.sleep(1)

# Functie voor de tweede thread
def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print("Thread 2: ", letter)
        time.sleep(1)

# Threads initialiseren
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# Start de threads
thread1.start()
thread2.start()

# Wacht tot beide threads klaar zijn
thread1.join()
thread2.join()

print("Beide threads zijn klaar.")