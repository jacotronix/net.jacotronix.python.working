#Given an array of integers, find the pair of adjacent elements that has the largest product and return that product.

#Example

#For inputArray = [3, 6, -2, -5, 7, 3], the output should be
#adjacentElementsProduct(inputArray) = 21.

#7 and 3 produce the largest product.

#Input/Output

#[time limit] 4000ms (py)
#[input] array.integer inputArray

#An array of integers containing at least two elements.

#Constraints:
#3 ? inputArray.length ? 10,
#-50 ? inputArray[i] ? 1000.

#[output] integer

#The largest product of adjacent elements.

def adjacentElementsProduct(inputArray):
    num = 0;
    length = len(inputArray) - 1;
    while (num < length):
        thisprod = inputArray[num] * inputArray[num+1];
        if (num == 0):
            product  = thisprod;
        elif (thisprod > product):
            product = thisprod;
        num += 1;
    return (product);

print adjacentElementsProduct([3, 6, -2, -5, 7, 3]);
print adjacentElementsProduct([5, 1, 2, 3, 1, 4]);
print adjacentElementsProduct([1, 2, 3, 0]);
print adjacentElementsProduct([4, 1, 2, 3, 1, 5]);
print adjacentElementsProduct([5, 6, -4, 2, 3, 2, -23]);
print adjacentElementsProduct([1, 2, 3]);
print adjacentElementsProduct([-50, -49, -48]);
print adjacentElementsProduct([1000, 1000, 1000]);
print adjacentElementsProduct([0, 0, 0]);
print adjacentElementsProduct([0, -50, 1000]);
print adjacentElementsProduct([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]);
print adjacentElementsProduct([1, 1]);
print adjacentElementsProduct([-20,1,20]);
print adjacentElementsProduct([-50,1,-10]);





