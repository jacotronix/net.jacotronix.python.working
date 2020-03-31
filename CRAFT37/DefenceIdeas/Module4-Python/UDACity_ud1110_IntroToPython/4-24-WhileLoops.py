card_deck = [4, 11, 8, 5, 13, 2, 8, 10]
hand = []

# adds the last element of the card_deck list to the hand list
# until the values in hand add up to 17 or more
while sum(hand)  < 17:
    hand.append(card_deck.pop())
print(hand)

###################################

# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# track the current number being multiplied
current = 1
# write your while loop here
while (current <= number):
    # multiply the product so far by the current number
    product *= current
    # increment current with each iteration until it reaches number
    current += 1
# print the factorial of number
print(product)

###################################


# number to find the factorial of
number = 6   
# start with our product equal to one
product = 1
# write your for loop here
#for current in range(number):
#    product *= current+1
for num in range(2, number + 1):
    product *= num
# print the factorial of number
print(product)

###################################

start_num = 0 # provide some start number
end_num = 9 #provide some end number that you stop when you hit
count_by = 4 #provide some number to count by 

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num

break_num = start_num
while(break_num < end_num):
    break_num += count_by

print(break_num)

###################################

start_num = 5 #provide some start number
end_num = 100 #provide some end number that you stop when you hit
count_by = 2 #provide some number to count by

result = "" 

# write a condition to check that end_num is larger than start_num before looping

if start_num > end_num:
    result = "Oops! Looks like your start value is greater than the end value. Please try again."

# write a while loop that uses break_num as the ongoing number to 
#   check against end_num
else:
    break_num = start_num
    while break_num < end_num:
        break_num += count_by
    result = break_num

print(result)

###################################
#Write a while loop that finds the largest square number less than an integerlimit and stores it in a variable nearest_square. A square number is the product of an integer multiplied by itself, for example 36 is a square number because it equals 6*6.

#For example, if limit is 40, your code should set the nearest_square to 36.

limit = 40

# write your while loop here

#nearest_square = 0
#index = 1
#while (index**2) <= limit:
#    nearest_square = index**2
#    index += 1

limit = 40

num = 0
while (num+1)**2 < limit:
    num += 1
nearest_square = num**2

print(nearest_square)

###################################
#Question: You need to write a loop that takes the numbers in a given list named num_list:
#num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

#Your code should add up the odd numbers in the list, but only up to the first 5 odd numbers together. If there are more than 5 odd numbers, you should stop at the fifth. If there are fewer than 5 odd numbers, add all of the odd numbers.
#num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]
#odd_numbers = []
#pointer = 0
#result = 0
#while len(odd_numbers) < 5:
#    if num_list[pointer] % 2 == 1:
#        odd_numbers.append(num_list[pointer])
#        result += num_list[pointer]
#    pointer += 1
        
#print(result, odd_numbers) 

num_list = [422, 136, 524, 85, 96, 719, 85, 92, 10, 17, 312, 542, 87, 23, 86, 191, 116, 35, 173, 45, 149, 59, 84, 69, 113, 166]

count_odd = 0
list_sum = 0
i = 0
len_num_list = len(num_list)

while (count_odd < 5) and (i < len_num_list): 
    if num_list[i] % 2 != 0:
        list_sum += num_list[i]
        count_odd += 1
    i += 1

print ("The numbers of odd numbers added are: {}".format(count_odd))
print ("The sum of the odd numbers added is: {}".format(list_sum))      