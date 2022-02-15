# Program to create grade calculator in Python
# By Vinay Tajane on 15th Feb 2022
Marks=dict()
Marks ={'Maths':0,'science':0,'Social-Studies':0,'English':0,'2nd Language':0}
Total=0

for i in Marks:
    mark = int(input('Enter Marks in '+i+':'))
    if mark>100 or mark<0:
        print("!!!!!!!Invalid Marks!!!!!!!\nTry Again('_')")
        quit()

    Marks[i]=mark
    Total+=mark
percentage = (Total/500)*100

print("\n===============================================")
print("Score:",Marks)
print("You Got",Total,"Out of 500!")
print("Your Percentage is:",percentage,'%')
if percentage>90:
    print("Your Grade is 'A+'")
elif percentage >80:
    print("Your Grade is 'A'")
elif percentage >75:
    print("Your Grade is 'B+'")
elif percentage >70:
    print("Your Grade is 'B'")
elif percentage >65:
    print("Your Grade is 'C+'")
elif percentage >60:
    print("Your Grade is 'C'")
elif percentage >55:
    print("Your Grade is 'D+'")
elif percentage >50:
    print("Your Grade is 'D'")
else:
    print("You are Fail -_-")
print("===============================================\n")
