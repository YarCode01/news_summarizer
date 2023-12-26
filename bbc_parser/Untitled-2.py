
class Vehicle:

    def __init__(self, brand = "honda"):
        self.brand = brand
        self.x = 0
    
    def drive(self):
        self.x += 1


class MessageTranscription:
    
    some_constant = 3.14 

    def transfrom_from_phone(str):
        return str[::-1]
    



honda = Vehicle()
honda.drive()
print(honda.x)