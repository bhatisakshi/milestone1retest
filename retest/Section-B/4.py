#Question-4: Sort python dictionareis by key:

new_dict={}
value=int(input("Enter the no. of key-value pairs you want to enter: "))
for i in range(1,value+1):
    print(f"For pair{i}: ")
    name=input("Enter key name: ")
    value=input("Enter key value: ")
    new_dict[name]=value
    
print(f"Original: {new_dict}")
new_dict=sorted(new_dict.items())
print(f"Sorted: {new_dict}")