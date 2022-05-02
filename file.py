num1 = 42 # variable declaration   
num2 = 2.3 # variable declaration
boolean = True # type check
string = 'Hello World' # variable declaration
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list of strings
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') #tuple
print(type(fruit)) # type check/ log statment
print(pizza_toppings[1]) # log statement/ access value
pizza_toppings.append('Mushrooms') # add value to list
print(person['name']) # log statement / access item from dictionary  
person['name'] = 'George' #dictionary change item
person['eye_color'] = 'blue'# dictionary add item
print(fruit[2]) # log statement from tuple 

if num1 > 45: # conditional if statement
    print("It's greater") # log statement 
else: # conditional else statement
    print("It's lower") # log statement

if len(string) < 5: # conditional if statement
    print("It's a short word!") # log statement
elif len(string) > 15: # conditional else if statement
    print("It's a long word!") # log statement
else: # conditional else statement
    print("Just right!") # log statement

for x in range(5): """ for loop with log statement
    print(x)
for x in range(2,5): 
    print(x)
for x in range(2,10,3):
    print(x)      for loop with log statement """
x = 0 # variable declaration loop start 
while(x < 5): # while loop end at less than 5  
    print(x) # log statement
    x += 1 # incrementation

pizza_toppings.pop() # list delete value 
pizza_toppings.pop(1) # list delete value 

print(person) # log statement / dictionary
person.pop('eye_color') # remove value from dictionary 
print(person) # log statment/ dictionary 

for topping in pizza_toppings: # for loop 
    if topping == 'Pepperoni': # if statement 
        continue # continue 
    print('After 1st if statement') # log statement 
    if topping == 'Olives': # if statement 
        break # break 

def print_hello_ten_times(): # function
    for num in range(10): # for loop
        print('Hello') # log statement

print_hello_ten_times() # calling function

def print_hello_x_times(x): # function
    for num in range(x): # for loop 
        print('Hello') # log statement

print_hello_x_times(4) # return value 

def print_hello_x_or_ten_times(x = 10): # function
    for num in range(x): # for loop 
        print('Hello') # log statement 

print_hello_x_or_ten_times() # calling function
print_hello_x_or_ten_times(4) # return value 


"""
Bonus section
"""

# print(num3) - name error 
# num3 = 72 - variable declaration 
# fruit[0] = 'cranberry' - tuple change value 
# print(person['favorite_team']) - key error 
# print(pizza_toppings[7])  - index error 
#   print(boolean) - indentation error
# fruit.append('raspberry') - attribute error tuple object has no attribute append
# fruit.pop(1) - tuple delete value 
