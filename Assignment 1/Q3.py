# Program to find Volume of sphere with 12 cm diameter
d = int(input("Enter the diameter of sphere: "))
r = d/2
def volume(x):
    v = 4/3 * 3.14 * (x**3)
    return v
if __name__ == "__main__":
    print("Volume: ",volume(r))