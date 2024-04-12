#Question-6: Set operations:
set1=set(x for x in input("Enter set1 elements separated by comma: ").split(','))
set2=set(x for x in input("Enter set2 elements separated by comma: ").split(','))
print("Sets: ")
print(set1)
print(set2)

set1.intersection(set2)
print(f"Intersection: {set1}")

set4=set1.union(set2)
print(f"Union: {set4}")

set4=list(set4)
set4=sorted(set4,reverse=True)
print("Maximum element: ",set4[0])

set5=sorted(set4)
print("Minimum element: ",set5[0])


