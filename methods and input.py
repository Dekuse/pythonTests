#degining a method
def method1():
    print("this is a test for a method")

def method2(value1,value2):
    value3=value1*value2
    #returning a value
    return value3

def method3(value1,value2,value3=''):
    #assuming value1 is a list
    for val in value1:
        print(val)

    #assuming value 2 is a dictionary
    for key,value in value2.items():
        print(value)

#method1()
#accecpting input from users
val1=input("insert a value")
val2=input("insert the second value")
finalvalue=method2(int(val1),int(val2))
#print(finalvalue)
dictt={"key1":"val1","key2":"val2"}
method3(list(range(2,5)),dictt)
#sending a list and dictionary to a method

