# Sum of Cubes
# By Vinay Tajane on 3rd March 2022
print("==== Find Sum of Cubes of First n Numbers ====")
n = int(input('Enter Number:'))
add = 0
for i in range(n+1):
    add = add +i**3
print("Sum of Cubes of First",n,"Numbers is",add)
