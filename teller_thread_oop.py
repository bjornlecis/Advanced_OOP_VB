import threading
import time

class Teller(threading.Thread):
    def __init__(self):
        super().__init__()
        self._teller = 0
        self._running = True
        self._lock = threading.Lock()

    def run(self):
        while self._running:
            with self._lock:
                self._teller += 1
            time.sleep(1)

    def stop(self):
        self._running = False

    def get_value(self):
        with self._lock:
            return self._teller

# Maak een Teller object aan
teller = Teller()

# Start de teller thread
teller.start()

# Wacht enige tijd om de teller te laten verhogen
time.sleep(5)

# Stop de teller thread
teller.stop()

# Wacht tot de teller thread is gestopt
teller.join()

# Print de uiteindelijke waarde van de teller
print("De uiteindelijke waarde van de teller is:", teller.get_value())