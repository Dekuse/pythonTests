"""this is a physical class describing a persons physical appearance 
"""
class physical:
    def __init__(self,height,weight,bmi):
        self.height=height
        self.weight=weight
        self.bmi=bmi
    def show_physical(self):
        physical=f"the hieight is {self.height} and the weight is {self.weight} and finally bmi is {self.bmi}"
        print(physical)