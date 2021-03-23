#creating a dictionary
dict={"one":"value one","two":"value two"}
print(dict)

#creating and trying multiple lists
list1=list(range(0,25))
print(list1)

list2=list(range(0,25,2))
print(list2)
list3=[]
for ls in list1:
    if ls in list2:
        list3.append(ls)
        print(ls)

print(list3)

listdict={"listone":list1,"list2":list2,"list3":list3}
print(listdict)
list4=list()
#iterating through the dictionalry of lists

for keys,value in listdict.items():
    if keys=="listone":
        for values in value:
            if (values%3==0) :
                list4.append(values)
                print (list4)

#knowing the length of a list and dictionary
print(len(list4))
print(len(listdict))
del list4[2]
print(list4)
del listdict["list3"]
print(listdict)