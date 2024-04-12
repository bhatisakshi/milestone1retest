#Question-1: Swap two numbers in a list

mylist=[int(x) for x in input("Enter elements of list in comma separated format: ").split(',')]
pos1=int(input("Enter position1: "))
pos2=int(input("Enter position2: "))

x=mylist[pos1]
mylist[pos1]=mylist[pos2]
mylist[pos2]=x

print(mylist)

