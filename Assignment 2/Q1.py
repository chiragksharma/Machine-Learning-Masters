# try:
#     # Some Code
# except:
#     # Executed if error in the
#     # try block
# else:
#     # execute if no exception

def divide():
    return 5 / 0


# ZeroDivisionError is a built-in Python exception thrown when a number is divided by 0

try:
    divide()
except ZeroDivisionError as ze:
    print("Don't divide By Zero!!!, Take some other number")
except:
    print("Any other exception")
