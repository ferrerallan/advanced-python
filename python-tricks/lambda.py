from ast import Lambda

duply = eval("lambda a,b:a*b")
print(duply(2,3))

#applying taxes on a list with map
prices = [100,500,10,30]
taxes = list(map(lambda a:a*0.3, prices))
print(taxes)

#transforming list in a dict for json
IDList= [1,2,3]
jsonMapped = list(map(lambda x:{"id":x,"name":f"user{x}"},IDList))
print(jsonMapped)