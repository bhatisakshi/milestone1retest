#Question-8: read last n ines of a file:

file=input("Enter filename: ")
n=int(input("Enter no. of last n lines you want to read: "))
with open(file,'r') as f:
    lines=f.readlines()
    last_n_lines=lines[-n:]
 
for line in last_n_lines:   
    print(line,end='')
    
