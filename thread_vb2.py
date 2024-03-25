def print_letters():
    for letter in ['a', 'b', 'c', 'd', 'e']:
        print("Thread 2: ", letter)
        time.sleep(1)

        # Onderbreek thread 1 na het printen van 'c' voor 3 seconden
        if letter == 'c':
            print("Thread 2 onderbreekt Thread 1 voor 3 seconden.")
            time.sleep(3)  # Pauzeer deze thread voor 3 seconden
            print("Thread 2 hervat Thread 1.")

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