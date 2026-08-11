import time
import threading
from concurrent.futures import ThreadPoolExecutor

# from concurrent.futures import ThreadPoolExtractor enables the creation of pool of Threads
# without manually creating each threads. You state the number of threads in
# ThreadPoolExecutor(max_workers=2) where max_workers is the number of Threads you want. In this case 2 Threads.
# In executor.submit(name, 2) the name represents the name of a function (in this case name),
# while 2 represents the paramenter name expects
def name(a):
    if a == 2:
        print("The Frist Thread")
    else:
       print("The Second Thread")
 

    for _ in range(a):
        a *= 2
    return a

if __name__ == "__main__":

    with ThreadPoolExecutor(max_workers=2) as executor:
        futures = [executor.submit(name, x) for x in [2, 4]]

        for y in futures:
            print(y.result())
    print("\nWe have come to the end of all Thread")