from threading import Thread
import time

def square_number():
    for i in range(100):
        i * i
        time.sleep(0.1)


th = []
num_th= 10

for i in range(num_th):
    p = Thread(target=square_number)
    Thread.append(p)

for p in th:
    p.start()

for p in th:
    p.join()

print("end main")