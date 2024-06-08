# in this program, you can shop items of your choice and it serves your total bill 

import random
class Shopping:
    def __init__(self) -> None:
        self.shopping_cart = {}

    def add_item(self, item, price):
        self.shopping_cart[item] = price
        print(f'{item} is added to your cart.\n')
        
    def remove_item(self, item):
        if item in self.shopping_cart:
            self.shopping_cart.pop(item)
            print(f'{item} has been removed from your cart.\n')
        else:
            print(f'{item} not found in your cart.\n')
        
    def calculate_bill(self):
        bill = 0
        for val in self.shopping_cart.values():
            bill += val
        
        print('Your purchased items:', ', '.join(self.shopping_cart))
        print('\nYour total bill is Rs.', bill)

shop = Shopping() # eggs
while True:
    decision1 = input('Would you like to continue to shop? (y/n): ')
    if decision1 != 'y':
        print('\nThank you for shopping with us!')
        break
    item = input('What item would you like to purchase?: ') #eggs
    price_range = range(100, 501) # eg: 367
    price = random.choice(price_range)

    shop.add_item(item, price)

    decision2 = input('Would you like to remove an item from your cart? (y/n): ')
    if decision2 == 'y':
        remove = input('What item would you like to remove?: ')
        shop.remove_item(remove)
    elif decision2 == 'n':
        print('You have decided not to remove any item from your cart.\n')
    else:
        print('Please enter y or n')
        
shop.calculate_bill()
print('Have a lovely day!')