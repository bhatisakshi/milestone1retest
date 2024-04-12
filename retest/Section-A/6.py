#Question-6: What will be the output of the following code?

def addItem(listParam):
    listParam+=[1]
    
mylist=[1,2,3,4]
addItem(mylist)
print(len(mylist))