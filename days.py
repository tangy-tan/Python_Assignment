# Main Function
def main():
    #ask the user input
    day = int(input("Enter a number between 1-7: "))
    # Display the return value of day_checker function
    print(day_check(day))

def day_check(day):
    # Match case statement 
    match day:
        case 1: 
            return "Monday" 
        case 2:
            return "Tuesday" 
        case 3:
            return "Wednesday" 
        case 4:
            return "Thursday" 
        case 5:
            return "Friday" 
        case 6:
            return "Saturday" 
        case 7:
            return "Sunday" 
        case _:
            return "Invalid Input" #default case
main()  #Runs the main function