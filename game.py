def main():
    num = 17  #number to be guessed
    while True:
            g = int(input("Enter your guess(or enter -1 to quit): "))

            if g == -1:
                print("Game exited.")
                break  
            if g < 0:
                print("Negative numbers (except -1) are not allowed. Try again.")
                continue  
            if g == num:
                print("YOU GOT IT🥳")
                break 
            else:
                print("Wrong guess, try again.")
main()