#Question-12: Use lambda in list comprehension for creating two new lists, even and odd from a given list:

mylist=[int(x) for x in input("Enter list elements separated by comma: ").split(',')]
new_list1=[x for x in filter(lambda item: item%2==0,mylist)]
new_list2=[x for x in filter(lambda item: item%2!=0,mylist)]
print(new_list1)
print(new_list2)