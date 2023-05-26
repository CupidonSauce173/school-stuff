# School project LAB-1 \ Binary to DEC - DEC to Binary


# Function to convert a decimal number to binary.
# given a length to not surpass (error when higher than can hold).
# number = number to convert.
# model  = length of the number.
def convertToBinary(number, model):
    print("Def called with success.")
    binaryString = ""
    while(number != 1):
        if(number % 2 == 0):
            binaryString = "0" + binaryString
            number = number / 2
        else:
            binaryString = "1" + binaryString
            number = (number - (number % 2)) / 2
    # number = 1, add 1 to binaryString
    binaryString = "1" + binaryString
    if(len(binaryString) > model):
        print("You have entered a too high number for the model.")
        return
    else:
        print(binaryString)
    print("converting to actual value...")
    # Might not take all the space (model being higher than the given number...Adding zeros.)
    remaining = model - len(binaryString)
    while(remaining != 0):
        binaryString = "0" + binaryString
        remaining -= 1
    print("real value: " + binaryString)
    print(str(model) + "bits value")

# Function to convert a binary to a decimal, base 2
# binary = binary to convert
def convertToDecimal(binary, base):
    # example : 1001 1011
    n = len(str(binary))
    print(n)
    i = 1
    table = []
    while(i < n):
        table.append(i * base)
        i += 1
    orderedTable = []
    i = -1
    for val in table:
        print(n - i)
        orderedTable.append(table[n - i])
        i += 1
    print("-------------------")
    for val in orderedTable:
        print(val)
convertToDecimal(10011011, 2)

print("Conversion Calculator, Binary base n -> Dec \ Dec -> Binary base n \n")
choice = input("Which conversion would you like? B Binary Dec, D Dec Binary, B\D: ")
if(choice == 'B' or choice == 'b'):
    print("Entered Binary to Dec mode.")
elif(choice == 'D' or choice == 'd'):
    print("Entered Dec to Binary.")
else:
    print("Input incorrect.")
    exit()

number = int(input("Please input an number to convert: "))
bits = int(input("Please input the length (2, 8, 16, 32 or 64): "))

if(bits != 2 and bits != 8 and bits != 16 and bits != 32 and bits != 64):
    print("Please select one of the given bits.")
    exit()
convertToBinary(number, bits)