def isValidInput(bin_str):
    """checks if inputted value is binary (0 and 1) and if the number of bits is less than 5"""
    
    undsc_bin = bin_str.replace("_", "")

    if len(undsc_bin) <= 5 and all(char in "01" for char in undsc_bin):
        return True

def bin2dec(bin_str):
    """converts binary to decimal without using int function""" 

    undsc_bin = bin_str.replace("_", "")
    reverse_bin = undsc_bin[::-1]
    dec = 0
    
    for digit, char in enumerate(reverse_bin):
        if char == "1":
            dec += 2 ** digit
    
    return dec

"""converts binary to decimal and prints reverse of the binary number and the converted decimal value (else, it shows invalid input)"""

bin_num = input("Please enter a binary number: ")

if isValidInput(bin_num):
   
    dec = bin2dec(bin_num)
    undsc_bin = bin_num.replace("_", "")
    reverse_bin = undsc_bin[::-1]
    print(reverse_bin)
    print(bin_num, "in decimal is", dec)

else:
    print("Invalid input: Please make sure the inputted number is a binary number and is only 5 bits long.")