#Data structures

clothes = []
clothes.append("T shirt")
clothes.append("Shirt")
clothes.pop() 
print(clothes)
"""
Stack~LIFO~Clothes wearing and removing
Queue ~waiting line~FIFO
Queue:
"""
lines = [ 'Putin', 'Trump', 'Kim Jong', 'Merkel'] 
first = lines.pop(0) 
second = lines.pop(0) 
print(first) 
print(second)
#Dictionaries
"""Accessing value in a dict."""
result = {'John' : 81, 'Tim' : 91}
print(result ['Tim'])
#Appending dict key & value
result = {'John' : 81, 'Tim' : 91, 'Bill' : 68}
result['Bill'] = 75
print(result)
#Deleting specific key & value
scores = {'John' : 81, 'Tim' : 91, 'Bill' : 75}
del scores['John']
print(scores)

