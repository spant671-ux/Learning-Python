#errors
#syntax error
#indentation error
#tab error

# print("Hello World"

# a = 12
# if a == 12:
# print("Hello")

#Exceptions

# a = int(input("Tell your number: "))
# print(10/a)
# print("Okay I have run the division!")

#try, except, else, finally, raise

a = int(input("Tell your number: "))

try:
    print(10/a)
except ZeroDivisionError:
    print("Sorry you cannot divide by 0.")