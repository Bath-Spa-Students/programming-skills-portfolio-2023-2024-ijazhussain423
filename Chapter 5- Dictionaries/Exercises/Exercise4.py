"""
Chapter 5, Exercise 4: Rivers ☑️

Make a dictionary containing three major rivers and the
 country each river runs through. One key-value pair might be 'nile':
   'egypt'.Use a loop to print a sentence about each river, such as 
   The Nile runs through Egypt.Use a loop to print the name of each
     river included in the dictionary.Use a loop to print the name of
       each country included in the dictionary.
"""

rivers={
        'Jhelum River':'Pakistan',
        'Kabul River':'Afghanistan',
        'Kizilirmak River':'Turkey',
        'yangtze':'china',
        'Koshi River':'Nepal',
        }

for river, country in rivers.items():
    print(f"the{river.title()}flos through{country.title()}.")
    
    print("\nthe following countries are include in this data set:")
    for country in rivers.values():
        print(F"-{country.title()}")
        
    print("\nthe following rivers are include in this data set:")
    for river in rivers.keys():
            print(F"-{river.title()}")