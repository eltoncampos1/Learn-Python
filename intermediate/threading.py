from threading import Thread, Lock
import time

db_value = 0

def increase(lock):
    global db_value
    lock.acquire()
    local_cp = db_value
    local_cp += 1
    time.sleep(0.1)
    db_value = local_cp
    lock.release()

if __name__ == "__main__":
    l = Lock()
    print('start value', db_value)
    th_1 = Thread(target=increase, args=(l,))
    th_2 = Thread(target=increase, args=(l,))
    th_1.start()
    th_2.start()
    
    th_1.join()
    th_2.join()

    print("end value", db_value)