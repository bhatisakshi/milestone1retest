#Question-7: Count total digits in number without taking string:

num=int(input("Enter number: "))
count=0
while num>0:
    num//=10
    count+=1
print(count)
    