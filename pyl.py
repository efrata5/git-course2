'''
some example of class
'''
class Car:
    '''
    i am explaianing about my future car
    '''
    def __init__(self,color ,brand):
        '''
        colors and brands
        '''
        self.color=color
        self.brand=brand
    def brands(self):
        print(f" i have a car it {self.color} and it is a brand {self.brand}")
SUZI=Car("Red","Vitis")
SUZI.brands()