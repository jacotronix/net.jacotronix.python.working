#Given an array of integers, calculate which fraction of its elements are positive, which fraction of its elements are negative, and which fraction of its elements are zeroes, respectively. Print the decimal value of each fraction on a new line.

#Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with absolute error of up to  are acceptable.

#Input Format

#The first line contains an integer, , denoting the size of the array. 
#The second line contains  space-separated integers describing an array of numbers .

#Output Format

#You must print the following  lines:

#A decimal representing of the fraction of positive numbers in the array.
#A decimal representing of the fraction of negative numbers in the array.
#A decimal representing of the fraction of zeroes in the array.

n = 6;
arr = [-4, 3, -9, 0, 4, 1,];

plus = 0.0;
zero = 0.0;
minus = 0.0;

i = 0;
while i < n:
    if arr[i] > 0:
        plus += 1;
    elif arr[i] < 0:
        minus += 1;
    else:
        zero += 1;
    i += 1;


print ("%.6f" % (plus / n));
print ("%.6f" % (minus / n));
print ("%.6f" % (zero / n));
