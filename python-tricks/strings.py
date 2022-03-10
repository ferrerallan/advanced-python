#join
#Join all items in a tuple into a string, using a hash character as separator:
myTuple = ["apple","android","alln","1","30"]

x = ",".join(myTuple)

print(x)
#apple,android,alln,1,30

#array slice
'''
a[start:stop]  # items start through stop-1
a[start:]      # items start through the rest of the array
a[:stop]       # items from the beginning through stop-1
a[:]           # a copy of the whole array
'''
#There is also the step value, which can be used with any of the above:
'''a[start:stop:step] # start through not past stop, by step
'''

'''
IMPORTANT! in case of negative values, its consider the last element minus negative value,
for example:
    "allan"[:-2] => all
    "allan"[-2:] => an
'''


###mutate a string, given the position and character to change
def mutate_string(string, position, character):
    return string[:position].join(character).join(string[position:])
    
#determinate the number of times wich a substring exists in a string
#for example, 'cdc' occurs 2 times in 'acdcdc'
#creating a slice that represent the lenght of target substring
print("searching substring")
def count_substring(string, sub_string):
    lenSubstring = len(sub_string)
    nTotal=0
    targetSlice = slice(0,lenSubstring)
    for n in range(0,len(string)):
        searchedString = string[n:]
        if (searchedString[targetSlice]==sub_string):
            nTotal+=1
    return nTotal

#split x partition
'''
split cut the parameter passed, and generates all pieces of array.
example:
"fruta, casa, lago, carro".split(",") generates ["fruta","casa","lago","carro"]

and partition generates a tuple with 3 elements: before, main, after
example:
"fruta, casa, lago, carro".partition("lago") generates ("fruta, casa", "lago", "carro")
'''

