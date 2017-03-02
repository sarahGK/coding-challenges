1.
# Assume only one number that appears an odd number of times in the list
# if the lenght of list is n, then the time complixity is O(n) and space complixity is O(n)


def findOdd(list):
    # declare a dictionary with the number as the key and number of appearances as the value
    dict = {} 
    # define the dictionary
    for number in list:
        if number in dict:
            dict[number] = dict[number] + 1
        else:
            dict[number] = 1
    # find the number with an odd number of appearance and return it    
    for number in dict:
        if dict[number] % 2 == 1:
    return number

2.
# Assume only one is heavier and all the others weigh exactly the same.
# --- PROCEDURE ---#
# 1.Randomly choose one coin A and set it aside. Call the findOneHeavy function with the parameter of the rest coins. 
# 2.Evenly divide rest coins into two parts and use the balance scale to compare these two weights. 
# 3.If the scale is balanced, then the heavier one is A; otherwise choose the heavier part and repeat step 1.
# If the total number of coins is n, then the time complixity is log(n) and space complixity is constant-O(4).

from random import randint
# Define the recursive function findOneHeavy
def findOneHeavy(list):
    if len(list) == 1:
        return list[0]
    else:
        # A == -1 to mark the list can be divided equally,otherwise randomly assign a coin to A
        A = -1
        if len(list) % 2 == 1:
            index = randint(0,len(list))
            A = list[index]
            list.remove(A)
            
        mid = int(len(list)/2)
        left = findOneHeavy(list[:mid])
        right = findOneHeavy(list[mid:])
        if left > right:
            return left
        elif left < right:
            return right
        else:
            if A == -1:
                return left
            return A


