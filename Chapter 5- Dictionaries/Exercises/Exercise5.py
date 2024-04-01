"""

Chapter 5, Exercise 5: Pets ☑️

Make several dictionaries, where each dictionary represents a different pet. 
In each dictionary, include the kind of animal and the
owner’s name. Store these dictionaries in a list called pets. Next, 
loop through your list and as you do, print everything you know about

each pet


"""

#make an empty list t store the pets in.
pets={}

pet1={"Animal type": "Lion", "Onwer": "Hassan", "Pet name": "sheru", }
pet2={"Animal type": "Eagle", "Onwer": "Ali",   "Pet name": "Badshah"}
pet3={"Animal type": "Rabbit", "Onwer": "Arif", "Pet name": "Bunny"}
pet4={"Animal type": "Parrot", "Onwer": "Ijaz" ,"Pet name": "Mithuu"}


pets=[ pet1,pet2,pet3,pet4]
for pet in pets:
    print(f"\nAnimal type: {pet['Animal type']}")
    print(f"Onwer: {pet ['Onwer']}")
    print(f"Pet name: {pet ['Pet name']}")