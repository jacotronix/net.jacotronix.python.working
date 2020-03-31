book_title =  ['great', 'expectations','the', 'adventures', 'of', 'great', 'sherlock','holmes','the','great','gasby','hamlet','adventures','of','huckleberry','fin']

word_counter = {}

for word in book_title:
    if word not in word_counter:
        word_counter[word] = 1
    else:
        word_counter[word] += 1

print(word_counter)

########################################################

word_counter = {}

for word in book_title:
    word_counter[word] = word_counter.get(word, 0) + 1

print(word_counter)

########################################################

cast = {
           "Jerry Seinfeld": "Jerry Seinfeld",
           "Julia Louis-Dreyfus": "Elaine Benes",
           "Jason Alexander": "George Costanza",
           "Michael Richards": "Cosmo Kramer"
       }

print("Iterating through keys:")
for key in cast:
    print(key)

print("\nIterating through keys and values:")
for key, value in cast.items():
    print("Actor: {}    Role: {}".format(key, value))

#######################################################

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits, but you do not want to count the other items in your basket.

result = 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

##Iterate through the dictionary
#for fruit in fruits:
##if the key is in the list of fruits, add the value (number of fruits) to result
#    result += basket_items.get(fruit, 0)

for object, count in basket_items.items():
   if object in fruits:
       result += count

print(result)

##########################################################

# You would like to count the number of fruits in your basket. 
# In order to do this, you have the following dictionary and list of
# fruits.  Use the dictionary and list to count the total number
# of fruits and not_fruits.

fruit_count, not_fruit_count = 0, 0
basket_items = {'apples': 4, 'oranges': 19, 'kites': 3, 'sandwiches': 8}
fruits = ['apples', 'oranges', 'pears', 'peaches', 'grapes', 'bananas']

#Iterate through the dictionary
for key, value in basket_items.items():
#if the key is in the list of fruits, add to fruit_count.
    # if fruits.count(key):
    if key in fruits:
        fruit_count += value
#if the key is not in the list, then add to the not_fruit_count
    else:
        not_fruit_count += value

print(fruit_count, not_fruit_count)



