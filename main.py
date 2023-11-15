num = int(input("Please give me a 4-digit even number and the last digit is not 0: ")) # Ask for the number

if num >= 1000 and num <= 9999: # Check: 4-digit number
    if num % 2 == 0: # Check: Even
        if num % 10 == 0: # Check: Last digit is 0 or not
            print("NOT GOOD! The last digit is zero!")
        else:
            print("Fantastic!")
    else:
        print("That's not a even!")
else:
    print("NO! That's not a 4-digit number!")

quit()