#Exercise 2: Glossary ☑️

#A Python dictionary can be used to model an actual dictionary. However,
# to avoid confusion, let’s call it a glossary.
#Think of five programming words you’ve learned about
 #in the previous chapters. Use these words as the keys in your glossary,
# and store
#their meanings as values.
#Print each word and its meaning as neatly formatted output.
# You might print the word followed by a colon and then its meaning, or print
#the word on one line and then print its meaning indented on a second line. Use the newline 
#character (\n) to insert a blank line between
#each word-meaning pair in your output.  



glossary={
    'list':'A list of collection ina particular order',
    'variable': 'A container to store data values',
    'dictionary':'A collection of key value pairs',
    'comment': 'A not in a python that the python interpreter ignores',
    'loop':'Work through a collection of items, one at a time',
    }
word='list'
print(f"\n{word.title()}:{glossary[word]}")
word='variable'
print(f"\n{word.title()}:{glossary[word]}")
word='dictionary'
print(f"\n{word.title()}:{glossary[word]}")
word='comment'
print(f"\n{word.title()}:{glossary[word]}")
word='loop'
print(f"\n{word.title()}:{glossary[word]}")
