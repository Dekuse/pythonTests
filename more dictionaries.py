#dictionary with in dictionary
dict1={
    "kid":{
      "name":"kidus negash",
      "sex":"male" ,
      "age":26
    },
    "bereket":{
        "name":"bereket samuel",
        "sex":"male",
        "age":15
    },
    "papy":{
        "name":"fitsum",
        "sex":"male",
        "age":27
    }
}

for name,data in dict1.items():
    for key,data in data.items():
            print(f"this is key value {key} and data value is {data}")

