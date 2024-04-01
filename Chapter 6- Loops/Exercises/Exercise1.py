#Chapter 6, Exercise 1: Pizza Toppings ☑️
#Write a loop that prompts the user to enter a series of pizza toppings until 
#they enter a 'quit' value. As they enter each topping,
#print a message saying you’ll add that topping to their pizza.
print("Enter pizza toppings.Type'quit'to finish.")
while True:
    topping = input("Enter a topping: ")
    if topping == 'quit':
        break
    print("I'll add", topping, "to your pizza.")