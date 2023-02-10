from multiprocessing import Process
import os
import time

def square_number():
    for i in range(100):
        i * i
        time.sleep(0.1)


processess = []
num_p= os.cpu_count()

for i in range(num_p):
    p = Process(target=square_number)
    processess.append(p)

for p in processess:
    p.start()

for p in processess:
    p.join()

print("end main")