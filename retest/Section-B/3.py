#Question-3: create a list of tuples -each tuple having  the number and its square:

new_list=[]
mylist=[int(x) for x in input("Enter list elements separated by comma: ").split(',')]
for x in mylist:
    new_list.append((x, x**3))
    
print(new_list)