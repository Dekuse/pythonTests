value=1
value2=5
val=[]
for values in range(value,value2):
    val.append(values)
    print(values)

lists= list(range(2,10,3))
print(lists)
print(val)

#defining a list at one line
val2= [val/2 for val in range(2,12,2)]
print(val2)

