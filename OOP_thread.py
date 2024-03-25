import threading
import time

class Counter:
    def __init__(self):
        self.value = 0
        self.lock = threading.Lock()  # Lock object om racevoorwaarden te voorkomen

    def increment(self, increment_value):
        with self.lock:
            print("Thread {} verhoogt de teller met {}".format(threading.current_thread().name, increment_value))
            self.value += increment_value

    def get_value(self):
        with self.lock:
            return self.value

# Functie die de teller verhoogt met een bepaald aantal
def increment_counter(counter, increment_value):
    for _ in range(5):
        counter.increment(increment_value)
        time.sleep(1)

# Aanmaken van een Counter object
counter = Counter()

# Creëren van meerdere threads
threads = []
for i in range(3):
    thread = threading.Thread(target=increment_counter, args=(counter, i+1), name="Thread-{}".format(i+1))
    threads.append(thread)
    thread.start()

# Wacht tot alle threads klaar zijn
for thread in threads:
    thread.join()

# Print de uiteindelijke waarde van de teller
print("De uiteindelijke waarde van de teller is:", counter.get_value())