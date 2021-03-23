comment="a value is in it"
lists=["list1","list2","list3","list4"]
message=f"this is a list of lists {lists[1]}"
print(message)
#appending a value
lists.append("list5")
print(lists)
#inserting a value at index 0
lists.insert(0, "list0")
print(lists)
#removing a value from lists
del lists[4]
print(lists)
#poping a value from a list
poped_item=lists.pop(2)
print(lists)
#poping the last item
poped_item2=lists.pop()
print(lists)
#removing an item by value
removeditem=lists[2]
print(removeditem)
lists.remove(removeditem)
print(lists)

lists.append("list7")
lists.append("list8")

print(lists)

for  listt in lists:
    print(listt.title())
    print(listt.upper())
    print(listt.lower())

    
print(lists)
