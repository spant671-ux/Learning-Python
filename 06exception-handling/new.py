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
except Exception as err:
    print(f"Sorry there is an error as {err}.")

print("Okay I have done the division!")

b = input("Enter a word: ")

try: 
    print (10/b)
except Exception as err:
    print(f"Sorry there is an error as {err}.")
else: 
    print("There is no exceptions!")
finally: 
    print("I will run no matter what!")
    
print("Done!")
