#Consider a staircase of size :
#   #
#  ##
####
#####
#Observe that its base and height are both equal to , and the image is drawn using # symbols and spaces. The last line is not preceded by any spaces.
#Write a program that prints a staircase of size .
#Input Format
#A single integer, , denoting the size of the staircase.
#Output Format
#Print a staircase of size  using # symbols and spaces.
#Note: The last line must have  spaces in it.
#Sample Input
#6 
#Sample Output
#     #
#    ##
#   ###
#  ####
######
#######
#Explanation
#The staircase is right-aligned, composed of # symbols and spaces, and has a height and width of .


#n = 6

for i in range(n):
    op = ""
    spaces = n-i-1
    hashes = i
    j = k = 0
    while j < spaces:
        op += " "
        j += 1
    while k <= hashes:
        op += "#"
        k += 1
    print op
