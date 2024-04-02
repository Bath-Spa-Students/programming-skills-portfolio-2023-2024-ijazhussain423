#Exercise 3: Glossary 2 ☑️

#Now that you know how to loop through a dictionary, clean up the code 
#from Exercise 6-3 (page 99) by replacing your series of print()
#calls with a loop that runs through the dictionary’s keys and values. 
#When you’re sure that your loop works, add five more Python terms
#to your glossary.When you run your program again, these new words and
#meanings should automatically be included in the output.



glossary ={
'Conditional test':'A comparsion between two values',
'ket':'A First item in a key_value pair in a distionary',
'Bloan expersion':'An expression that evaluates to true or false',
'list':'A list of collection in a particular order',
'Loop':'Work through a collection of items,one at a time',
'dictionary':'A collection of key_value pairs',
'string':'good as a reaction',
'Value':'An item associated with a key in a distionary',
'Float':'A numerical value with a decimal component',
'comment':'A not in a python that the python interpreter ignores',}
for word, definition in glossary.items():
    print(f"\n{word.title()}: {definition}")