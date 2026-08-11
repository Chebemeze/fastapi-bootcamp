import time
import threading

count = 0
def name(a):
    global count
    start = time.time()
    print(f"{a} is now executing")
    print("It is getting closer to the end.")

    #implementing GIL lock, so the count variable
    lock = threading.Lock()
    with lock:
        for _ in range(30000):
            count += 0.001

    elapse = time.time() - start
    print(f"Time spent running: {elapse}. It's the end of {a}\n")

if __name__== "__main__":
    thread1 = threading.Thread(target=name, args=("Thread1",))
    thread2 = threading.Thread(target=name, args=("Thread2",))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"It's the end of the main Thread, count is now : {count}")
