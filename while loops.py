#trying while loops with different conditions with lists
listone=list()
listtwo=list(range(1,25,2))
length=len(listtwo)
dictone={}
start=1
while listtwo and start<=length:
    dictone={start:listtwo.pop()}
    start+=1
    print(dictone)

