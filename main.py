# Tuple items are enclosed in round brackets
# Tuple is ordered
# Tuple is immutable
# Tuple elements do not need to be unique
# Elements can be of different data types

'''
Creating a Tuple
'''

# tuple= ()
# tuple= ('cat',[1,2,3,4], (1,2,3))
# tuple= 1234, 4321
# tuple='hello',
# tuple=('hello',)
# print(tuple)

'''
Access Tuple Elements
'''
# tuple = (1234, 4321, 'hello')
# print(tuple[0])

'''
Negative Indexing
'''

# # Access with negative indexing
# tuple = (1234, 4321, 'hello!')
# tuple[-1] # output => 'hello'
# tuple[-3] # output => 1234

'''
Slicing Tuples in Python
'''
# fruits= ('orange', 'apple', 'pear', 'grapes', 'banana')
# print(fruits[:])
# print(fruits[2:5])
# print(fruits[:-2])
# print(fruits[:2])
# print(fruits[2:])
# print(fruits[::2])
# print(fruits[::-1])

'''
Changing a Tuple
'''
# fruits= ('orange', 'apple', 'pear', 'grapes', 'banana')
# fruits[0]='pear'


'''
Deleting a Tuple
'''
# fruits= ('orange', 'apple', 'pear', 'grapes', 'banana')
# # del fruits[0]
# # print(fruits)
# del fruits
# print(fruits)

'''
Tuple Methods
'''

#print(dir(tuple))

fruits= ('orange', 'orange', 'apple', 'pear', 'grapes', 'banana')
print(fruits.count('orange'))
print(fruits.index('apple'))