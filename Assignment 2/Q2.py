# List Comprehension
# It offers a shorter syntax when you want to create a new list based on the values of an existing list.

# newlist = [expression for item in iterable if condition == True]

subject = ["Americans ","Indians"]
verb = ["play","watch"]
object = ["Baseball","Cricket"]

newlist = [(sub+" "+ver + " " + obj + " ") for sub in subject for ver in verb for obj in object]

for sentance in newlist:
    print(sentance)