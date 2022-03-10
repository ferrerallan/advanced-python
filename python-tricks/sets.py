setA = set([1,1,3,4,6,7,7])
setB = {3,4}
print(setA & setB)

#union 
setA | setB 

#intersection
setA & setB

#diference
setA - setB

#with dicts
listFruitA = [ {
                "name":"abacate",
                "color":"green"
              },
              {
                "name":"pera",
                "color":"yellow"
              },
            ]

listFruitB = [ {
                "name":"abacate",
                "color":"green"
              }
            ]

listFruitA
intersectList = [item for item in listFruitA if item in listFruitB ]
print(intersectList)