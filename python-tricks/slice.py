'''
Slices are objects so they can be stored in variables. Some data structures allow for indexing and slicing such as lists, strings, and tuples.
We can use integers to specify the upper and lower bound of the slice or use a slice object.

slice allow to store a range of something
'''
s = slice(3,6)

list = [1, 3, 'a', 'b', 5, 11, 16]
text = 'DataScience'
tpl = (1,2,3,4,5,6,7)

print(list[s])

print(text[s])

print(tpl[s])
