#Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells them the year that
# they will turn 100 years old.

#Extras:
#Add on to the previous program by asking the user for another number
# and printing out that many copies of the previous message.
# (Hint: order of operations exists in Python)
#Print out that many copies of the previous message on separate lines.
# (Hint: the string "\n is the same as pressing the ENTER button)

name = str(input("What is your name ? "))
last_name = str(input("What is your last name ? "))
age = int(input("How old are you ? "))

print("Great! Your name is... " + '\n')
print(name.title() + " " +last_name.title())

yearnow = 2019
birthday = yearnow + (100 - age)

print("Your hundredth birthday will be in " , birthday)
