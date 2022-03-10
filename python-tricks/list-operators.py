simpleList = [1,2,3,4,5,5,6,7,8,9,10]

#sum
print(f"sum of list {sum(simpleList)}")

#max
print(f"sum of list {max(simpleList)}")

#min
print(f"sum of list {min(simpleList)}")

#number of times of a element in a list
print(f"number of times of 5: {simpleList.count(5)}")

#length of a list
print(f"length of list: {len(simpleList)}")

#filtering list with for
dataEven = [item for item in simpleList if item%2==0]
print(f"filtering with for: {dataEven}")

#remove
'''The remove() method removes the first matching element (which is passed as an argument) from the list.
'''
# create a list
prime_numbers = [2, 3, 5, 7, 9, 11]
# remove 9 from the list
prime_numbers.remove(9)


# Updated prime_numbers List
print('Updated List: ', prime_numbers)

# Output: Updated List:  [2, 3, 5, 7, 11]