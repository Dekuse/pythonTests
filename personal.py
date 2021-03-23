#simple class definition
""" this is a class to define a personal features and methods"""
class personal:
    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender
    def show_profile(self):
        profile=f"my name is {self.name}, my age is {self.age}, and i am {self.gender}"
        print(profile)
    def change_my_age(self,age):
        self.age=age
    def get_name(self):
        return self.name


