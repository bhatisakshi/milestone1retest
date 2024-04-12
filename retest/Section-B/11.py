#Question-11: time taken to execute a program:
import time
def mk(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  
        result = func(*args, **kwargs)  
        end_time = time.time()  
        time_taken = end_time - start_time  
        print(f"Function {func.__name__} executed in {time_taken:.4f} seconds.")
        return result
    return wrapper
    
def mk2():
    print("Ordinary")

p=mk(mk2)
p()    