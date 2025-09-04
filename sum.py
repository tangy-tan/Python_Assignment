def main():
    calc_sum()

def calc_sum():
    # Ask the user for input
    num = int(input("Enter the positive integer: "))
    # initalize the variable to store sum
    Even_Sum = 0
    for i in range(1, num + 1):
        if i % 2 == 0:  # To check if the number is even
            Even_Sum += i  # Adding even numbers

    print(f"Sum of even numbers from 1 to {num}: {Even_Sum}")

# Calling the main function
main()
