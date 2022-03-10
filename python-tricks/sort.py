#Consider we have a list of lists.
lst = [[2, 7], [7, 3], [3, 8], [8, 7], [9, 7], [4, 9]]

#We can sort the list based on the first or 
# second items of the inner lists by using the sort function with a lambda function.

lst.sort(key = lambda a:a[0])
#print(lst)


dictPersons = [{"name":"Allan", "age":39, "salary":1000},
               {"name":"Yan", "age":1 , "salary":2000} 
              ]
dictPersons.sort(key = lambda a:a["salary"])              

print(dictPersons)