""" this is a class that contains features and methods about a persons
property. """
from personal import personal
class property():
    def __init__(self,house,car,company):
        
        self.house=house
        self.car=car
        self.company=company
    def show_property(self):
        property=f"i have {self.house} and {self.car} and {self.company}"
        print(property)
    

        