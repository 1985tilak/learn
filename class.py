class Cookie:
    def __init__(self, color):
        self.color = color

    def get_color(self):
        return self.color
    
    def set_color(self,color):
        self.color = color

cookie_one = Cookie('green')
cookie_two = Cookie('red')

print(f'Cookie one is: {cookie_one.get_color()}')
print(f'Cookie two is: {cookie_two.get_color()}')


cookie_one.set_color('yellow')

num1 = 11
num2 = num1

print("\nbefore num2 is updated")

print("num1 address is", id(num1))
print("num2 address is", id(num2))

num2 = 12 

print("\nafter num2 is updated")

print("num1 address is", id(num1))
print("num2 address is", id(num2))

dict1 = {
    'value': 11
}

dict2 = dict1 

print("\nbefore value is updated")
print("dict1", dict1)
print("dict2", dict2)

print("\naddress of dict1", id(dict1))
print("address of dict2", id(dict2))

dict2['value'] = 22 

print("\nafter dict2 update")
print("dict1", dict1)
print("dict2", dict2)

print("\naddress of dict1", id(dict1))
print("address of dict2", id(dict2))



