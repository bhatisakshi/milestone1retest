#Question-17: What will be the ouput of the following expression?

my_string="I will score at least 60"
k=[]
for x in my_string.lower():
    if x not in "aeiou":
        k.append(x)
        
print(k)
        
k=[x for x in "I will score at least 60".lower() if x not in "aeiou"]
print(k)