import test
import errno
import multiprocessing
import time

try:
    p1 = multiprocessing.Process(target=test.testFun, name="test")
    p2 = multiprocessing.Process(target=test.testFun2, name="test")
    p1.start()
    p2.start()
    start = time.time()
    while time.time() - start <= 5:
        if (p1.is_alive() or p2.is_alive()):
            time.sleep(.1)  
        else:
            break
    else:
        p1.terminate()
        p2.terminate()
        p1.join()
        p2.join()
    '''test.testFun();'''
except:
    print(errno);
    
print("done")
