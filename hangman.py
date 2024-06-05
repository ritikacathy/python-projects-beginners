import random

def fruits():
    list_of_fruits = ['Apple', 'Banana', 'Cherry', 'Dates', 
                      'Elderberry', 'Fig', 'Guava', 'Hackberry', 
                      'Imbe', 'Jackfruit', 'Kiwi', 'Lemon', 
                      'Mango', 'Nectarine', 'Oranges', 'Passionfruit', 
                      'Quince', 'Raspberry', 'Strawberries', 'Tangerine', 
                      'Ugni', 'Vanilla', 'Watermelon', 'Xigua', 
                      'Yangmei', 'Zucchini']
    return random.choice(list_of_fruits).upper()


print('\nGuess the word! HINT: word is a name of a fruit\n')
# if Lemon is the word

fruit = fruits()
fruit = list(fruit)
#print(fruit)
length = len(fruit) # 5
print(' '.join(fruit))
print('_ ' * length)
