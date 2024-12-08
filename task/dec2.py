import time 

def timing_decorator(func): 
    def wrapper(*args, **kwargs): 
        start_time = time.time()  
        result = func(*args, **kwargs) 
        end_time = time.time()  
        print(f"time '{func.__name__}': {end_time - start_time:.2f} sec") 
        return result 
    return wrapper
@timing_decorator
def evenNum ():
    for x in range(0,100000):
        if x % 2 == 0:
            print(x) 

evenNum()