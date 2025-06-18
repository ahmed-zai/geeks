""""
Challenge 1

    Ask the user for a number and a length.
    Create a program that prints a list of multiples of the number until the list length reaches length.

Examples


number: 7 - length 5 ➞ [7, 14, 21, 28, 35]

number: 12 - length 10 ➞ [12, 24, 36, 48, 60, 72, 84, 96, 108, 120]

number: 17 - length 6 ➞ [17, 34, 51, 68, 85, 102]

"""



def get_inputs():
    while True:
        number_input = input("Enter a number: ")
        length_input = input("Enter the length: ")
        
        if  length_input.isdigit():
            number = int(number_input)
            length = int(length_input)

            
            if  length > 0:
                return number, length
            else:
                print(" the tow number must be possitive ")
        else:
            print("Invalid input pleas try agin ")

    
number, length = get_inputs()
        

multiples = [number * i for i in range(1, length + 1)]
print(f"\n the totala of  {number} (length {length}): {multiples}")
