from colorama import Fore, Style
from calculator import add, subtract, multiply, divide

def calculator():
    while True:
        print(Fore.CYAN + "Welcome to Raseroka's Calculator!")
        print("Choose an operation:")
        print(" ")
        print(Fore.GREEN + "1. Addition")
        print(Fore.YELLOW + "2. Subtraction")
        print(Fore.MAGENTA + "3. Multiplication")
        print(Fore.RED + "4. Division" + Style.RESET_ALL)

        choice = input("Enter your choice (1/2/3/4): ")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))

            if choice == '1':
                print(Fore.GREEN + f"The result is: {add(num1, num2)}" + Style.RESET_ALL)
            elif choice == '2':
                print(Fore.YELLOW + f"The result is: {subtract(num1, num2)}" + Style.RESET_ALL)
            elif choice == '3':
                print(Fore.MAGENTA + f"The result is: {multiply(num1, num2)}" + Style.RESET_ALL)
            elif choice == '4':
                print(Fore.RED + f"The result is: {divide(num1, num2)}" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Invalid choice. Please select a valid operation." + Style.RESET_ALL)
            continue  # Continue to the next iteration to let the user try again
        print(" ")

        continue_calculating = input(Fore.CYAN + "Do you want to perform another calculation? (Press Enter to exit, type 'yes' to continue): ")

        if continue_calculating.lower() != 'yes':
            print(Fore.YELLOW + "Thank you for using the calculator! Goodbye!" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    calculator()