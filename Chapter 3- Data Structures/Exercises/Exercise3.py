# Exercise 3: Your Own List :ballot_box_with_check:

#Think of your favorite mode of transportation, such as a motorcycle or a car, 
#and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a Honda 
#motorcycle.”

#The varaible 'transport_list' stores a list of vehicales. Each vehicale is given a statement
# and printed as output.
transport_list=['bike','civic','plane']

statement=f"I would like to own a Motor{transport_list[0].title()}"
print(statement)

statement=f"I would like to own a Honda{transport_list[1].title()}"
print(statement)

statement=f"I would like to own a Aero{transport_list[2].title()}"
print(statement)