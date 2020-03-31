
points = 174  # use this input to make your submission

# write your if statement here

prizes = ('wooden rabbit', 'no prize', 'wafer-thin mint', 'penguin')

result = ""
prize_string = "Congratulations! You won a %s!"

if (points <= 50):
    result = prize_string % prizes[0]
elif (points <= 150):
    result = "Oh dear, no prize this time."
elif (points <= 180):
    result = prize_string % prizes[2]
elif (points <= 200):
    result = prize_string % prizes[3]

print(result)

