#Question-2: Reverse words of a string:

string=[x for x in input("Enter string: ").split()]
string=reversed(string)
new_string=''
for x in string:
    new_string+= x +' '
    
print(new_string)