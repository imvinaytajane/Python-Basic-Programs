# Sum of Squares
# By Vinay Tajane on 3rd March 2022
print("==== Find Sum of Squares of First n Numbers ====")
n = int(input('Enter Number:'))
add = 0
for i in range(n+1):
    add = add +i**2
print("Sum of Squares of First",n,"Numbers is",add)
