# Made by Vinay on 05 Sept 2021
# Problem Statment
# Find the average of the second smallest and second greatest integer from given integers without using any pre-defined functions like sort,sorted(),etc
# input: 2,4,9,6,8,1
# Output: 5


set = [2,4,9,6,8,1]

#defining function to give smallest and largest value in set at that time
def smallergest():

    smallest = None
    largest = None

    for num in set:
      if largest == None:
        largest = num
      elif num > largest:
          largest = num

      if smallest == None:
        smallest = num
      elif num < smallest:
        smallest=num
    return smallest,largest

#Defining function of average of smallest and largest at that time
def avgerage():
    avg = (smallest + largest)/2
    return avg

smallest = smallergest()[0]
largest = smallergest()[1]

print("Smallest Number is:",smallest)
print("Largest Number is:",largest)
print("Average for Largest and Smallest is:",avgerage())

#removing largest and smallest so that new smallest and largest will second ones
set.remove(smallest)
set.remove(largest)

#new largest will be from remaining
smallest = smallergest()[0]
largest = smallergest()[1]

print("Second Largest Number is:",largest)
print("Second Smallest Number is:",smallest)
print("Average for Second Largest and Second Smallest is:",avgerage())


