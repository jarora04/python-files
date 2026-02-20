import threading
import time
from concurrent.futures import ThreadPoolExecutor
def func(n):
    print(f"the sleeping time is{n}")
    time.sleep(n)
    
#One of the method for multiprocessing
# t1=threading.Thread(target=func,args=[2])
# t2=threading.Thread(target=func,args=[3])
# t3=threading.Thread(target=func,args=[4])
# t1.start()
# t2.start()
# t3.start()

def poolingDemo():
    with ThreadPoolExecutor(max_workers=3) as executor:
        l=[2,5,6,8]
        result=executor.map(func,l)
        
        for i in result:
            print(i)
        

    
poolingDemo()
    