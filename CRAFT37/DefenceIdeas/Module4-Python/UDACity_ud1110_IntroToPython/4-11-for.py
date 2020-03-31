sentence = ["the", "quick", "brown", "fox", "jumped", "over", "the", "lazy", "dog"]

# Write a for loop to print out each word in the sentence list, one word per line

for word in sentence:
    print(word)

# Write a for loop using range() to print out multiples of 5 up to 30 inclusive

for num in range(5, 31, 5):
    print(num)


# Write a for loop that iterates over the names list to create a usernames list.
# To create a username for each name, make everything lowercase and replace spaces
# with underscores. Running your for loop over the list

names = ["Joey Tribbiani", "Monica Geller", "Chandler Bing", "Phoebe Buffay"]
usernames = []

# write your for loop here

#for index in range(len(names)):
#    names[index] = names[index].lower()
#    names[index] = names[index].replace(" ", "_")
#    usernames.append(names[index])
for name in names:
    usernames.append(name.lower().replace(" ", "_"))

print(usernames)


# Write a for loop that iterates over a list of strings, tokens, and counts how many
# of them are XML tags. XML is a data language similar to HTML. You can tell if a string
# is an XML tag if it begins with a left angle bracket "<" and ends with a right angle bracket ">".
# Keep track of the number of tags using the variable count.

tokens = ['<greeting>', 'Hello World!', '</greeting>']
count = 0

# write your for loop here

for item in tokens:
    if ((item[0] == '<') and (item[-1] == '>')):
        count += 1

print(count)


items = ['first string', 'second string']
html_str = "<ul>\n"  # "\ n" is the character that marks the end of the line, it does
                     # the characters that are after it in html_str are on the next line

# write your code here
for item in items:
    # html_str += '<li>' + item + '</li>\n'
    html_str += "<li>{}</li>\n".format(item)
html_str += "</ul>\n"

print(html_str)

print(list(range(4)))
print(list(range(4,8)))
print(list(range(4,10,2)))
print(list(range(0,-5)))

colors = ['Red', 'Blue', 'Green', 'Purple']
lower_colors = [ ]

for color in colors:
    #finish this part
    lower_colors.append(color.lower())

print(lower_colors)