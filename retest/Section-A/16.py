#Question-16: What will be the ouput of the following expression?

def mk(x):
    def mk1():
        print("Decorated")
        x()
    return mk1
    
def mk2():
    print("Ordinary")

p=mk(mk2)
p()    
        

