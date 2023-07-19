import pprint

message = 'It was a bright cold day and the clocks were striking thirteen.'

#Declare dictionary that will hold each letter key and # of times it appears
#as value
count = {}

for letter in message:
    #If there is no key with that letter, create one & set its value to 1
    if letter not in count:
      count.setdefault(letter, 1)
    #Else if there is such key, add 1 to its value
    elif letter in count:
      count[letter] += 1

#Print out the count dictionary
pprint.pprint(count)
