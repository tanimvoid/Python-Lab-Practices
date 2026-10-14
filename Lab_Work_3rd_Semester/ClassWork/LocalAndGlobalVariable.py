x = 10 # Global Variable

def my_function():
    global x # Define Global Variable
    x = x + 5 # Change Global Variable
    print("Inside Function", x)

my_function()
print("Outside Function", x)
