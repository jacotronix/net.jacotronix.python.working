#Below, you'll find two methods to solve the cargo loading program from the video. The first one is simply the one found in the video, which breaks from the loop when the weight reaches the limit. However, we found several problems with this. The second method addresses these issues by modifying the conditional statement and adding continue. Run the code below to see the results and feel free to experiment!

manifest = [("bananas", 15), ("mattresses", 24), ("dog kennels", 42), ("machine", 120), ("cheeses", 5)]

# the code breaks the loop when weight exceeds or reaches the limit
print("METHOD 1")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking loop now!")
        break
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

# skips an iteration when adding an item would exceed the limit
# breaks the loop if weight is exactly the value of the limit
print("\nMETHOD 2")
weight = 0
items = []
for cargo_name, cargo_weight in manifest:
    print("current weight: {}".format(weight))
    if weight >= 100:
        print("  breaking from the loop now!")
        break
    elif weight + cargo_weight > 100:
        print("  skipping {} ({})".format(cargo_name, cargo_weight))
        continue
    else:
        print("  adding {} ({})".format(cargo_name, cargo_weight))
        items.append(cargo_name)
        weight += cargo_weight

print("\nFinal Weight: {}".format(weight))
print("Final Items: {}".format(items))

##########################################
print("##########################################")

#Write a loop with a break statement to create a string, news_ticker, that is exactly 140 characters long. You should create the news ticker by adding headlines from the headlines list, inserting a space in between each headline. If necessary, truncate the last headline in the middle so that news_ticker is exactly 140 characters long.

#Remember that break works in both for and while loops. Use whichever loop seems most appropriate. Consider adding print statements to your code to help you resolve bugs.

# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
# write your loop here
#for line in headlines:
#    if (len(news_ticker) + len(line) + 1) <= 140:
#        news_ticker += (line + " ")
#    else:
#        news_ticker += (line[:(140 - len(news_ticker))])
#        break

for line in headlines:
    if (len(news_ticker) + len(line) + 1) <= 140:
        news_ticker += (line + " ")
    else:
        news_ticker += (line[:(140 - len(news_ticker))])
        break

print(len(news_ticker))
print(news_ticker)

##########################################
print("##########################################")

## Your code should check if each number in the list is a prime number
check_prime = [26, 39, 51, 53, 57, 79, 85]

## write your code here
## HINT: You can use the modulo operator to find a factor

for num in check_prime:
    count = 2
    while count < num:
        if (num%count) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, count, num))
            break
        else:
            count += 1
            if count == num:
                print("{} IS a prime number".format(num))  
  
# iterate through the check_prime list
for num in check_prime:
# search for factors, iterating through numbers ranging from 2 to the number itself
    for i in range(2, num):
# number is not prime if modulo is 0
        if (num % i) == 0:
            print("{} is NOT a prime number, because {} is a factor of {}".format(num, i, num))
            break
# otherwise keep checking until we've searched all possible factors, and then declare it prime
        if i == num -1:    
            print("{} IS a prime number".format(num))