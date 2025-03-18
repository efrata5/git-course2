'''
some example of class
'''
class Suzi_Car:
    '''
    i am explaianing about my future car
    '''
    def __init__(self, color , brand):
        '''
        colors and brands
        '''
        self.color=color
        self.brand=brand
    def brands(self):
      '''
      describe  the car brand and color
      '''
      print(f" i have a car it {self.color} and it is a brand {self.brand}")

CARS=Suzi_Car("Red","Vitis")
print(CARS.brands())