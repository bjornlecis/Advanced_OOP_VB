import threading
import time

# Functie voor de thread met parameters
def print_message(message, delay):
    for _ in range(5):
        print(message)
        time.sleep(delay)

# Thread initialiseren met parameters
thread = threading.Thread(target=print_message, args=("Dit is een bericht.", 3.2))

# Start de thread
thread.start()

# Wacht tot de thread klaar is
thread.join()

print("Thread is klaar.")