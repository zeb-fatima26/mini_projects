while True:
print("============== Calculator ==============")

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

print("Choose an option: ")
option = int(input("Select option:"))
if option not in [1, 2, 3, 4, 5]:
    print("Invalid choice")
    continue
if option == 5:
    print("Thankyou for using the calculator")
     break
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))


if option == 1:
    print("Result ", first_number + second_number)
elif option == 2:
    print("Result: ", first_number - second_number)
elif option == 3:
    print("Result: ", first_number * second_number)
elif option == 4:
    if second_number == 0:
        print("Cannot divide by zero")
    else:
        print("Result: ",first_number / second_number)
else:
    print("Invalid choice")
again = input("Do you want to perform another calculation? (Y?N): ")
if again.upper() == "N":
    print("Thank you for using this calculator!")
    break
