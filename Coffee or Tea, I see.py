# Programer Zeel Shah
# Student Number: 250970094
#"Coffee or Tea, I see" is designed to take a customers order, then output the order with the total cost.
#If the user inputs an invalid answer they will be exited from the program.
import sys
# Create Variables
nameOfCustomer = ()  # String
typeOfBeverage = ()  # String
sizeOfDrink = ()  # String
flavorInDrink = ()  # String
priceSize = 0.0 #float
priceFlavour = 0.0 #float
TAX=1.11 #constant

# Create menu
stars = "*" * 55
print(stars)
print("*                                                     *")
print("*                      MENU                           *")
print("*                                                     *")
print("*    COFFEE              Size             TEA         *")
print("*                     Small $1.50                     *")
print("*                     Medium $2.50                    *")
print("*                     Large $3.25                     *")
print("*    Flavours                         Flavours        *")
print("*    None      $0.00                  None  $0.00     *")
print("*    Vanilla   $0.25                  Lemon $0.25     *")
print("*    Chocolate $ 0.75                 Mint  $0.50     *")
print("*    Maple     $0.50                                  *")
print(stars)

# Prompt user to enter their name
nameOfCustomer = input("Welcome, please enter your name with no spaces ")
print()

# Check Input user adds for their name
if nameOfCustomer.isalpha():
    # Prompt user to enter their drink choice (Coffee or Tea)
    typeOfBeverage = input("Please choose the type of drink your would like to order (Coffee/C or Tea/T) ").lower()
    print()
    # Check input to see if the drink that they picked was valid
    if typeOfBeverage == "coffee" or typeOfBeverage == "c":
        typeOfBeverage = "coffee"
        # Prompt user to enter size of drink that they would like
        sizeOfDrink = input("Please enter the size of your choice ").lower()
        print()
        # Determine the size of the drink they chose
        if sizeOfDrink == "small" or sizeOfDrink == "s":
            sizeOfDrink = "small"
        elif sizeOfDrink == "medium" or sizeOfDrink == "m":
            sizeOfDrink = "medium"
        elif sizeOfDrink == "large" or sizeOfDrink == "l":
            sizeOfDrink = "large"
        else:
            print("Incorrect size entered. Goodbye.")
            sys.exit()
        #Prompt user to enter a flavour
        flavorInDrink = input("What flavour would you like added to your drink? (None/N, Maple/M, Chocolate/C or Vanilla/V )").lower()
        print()
        if flavorInDrink == 'none' or flavorInDrink == 'n' or flavorInDrink=="":
                flavorInDrink = 'no flavoring'
        elif flavorInDrink == 'vanilla' or flavorInDrink == 'v':
                flavorInDrink = 'vanilla'
        elif flavorInDrink == 'maple' or flavorInDrink == 'm':
                flavorInDrink ='maple'
        elif flavorInDrink== 'chocolate' or flavorInDrink == 'c':
                flavorInDrink ='chocolate'
        else:
                print("Incorrect flavour selected. Goodbye.")
                sys.exit()
    elif typeOfBeverage == "tea" or typeOfBeverage == "t":
        typeOfBeverage = "tea"
        sizeOfDrink = input("What size of drink would you like? ").lower()
        print()
        # Determine the size of the drink they chose
        if sizeOfDrink == "small" or sizeOfDrink == "s":
            sizeOfDrink = "small"
        elif sizeOfDrink == "medium" or sizeOfDrink == "m":
            sizeOfDrink = "medium"
        elif sizeOfDrink == "large" or sizeOfDrink == "l":
            sizeOfDrink = "large"
        else:
            print("Incorrect size entered. Goodbye.")
            sys.exit()
        # Prompt user to enter a flavour
        flavorInDrink = input("What flavour would you like added to your drink? (None/N, Mint/M or Lemon/L) ").lower()
        print()
        if flavorInDrink== 'none' or flavorInDrink == 'n' or flavorInDrink=='':
            flavorInDrink = 'no flavoring'
        elif flavorInDrink == 'lemon' or flavorInDrink == 'l':
            flavorInDrink = 'lemon'
        elif flavorInDrink == 'mint' or flavorInDrink == 'm':
             flavorInDrink = 'mint'
        else:
             print("Incorrect flavour entered. Goodbye.")
             sys.exit()
    else:
        print("Invalid beverage selected. Goodbye.")
        sys.exit()

else:
    print ("Invalid Input. Your name should only have letters with no spaces. Goodbye")
    sys.exit()

#Set prices
if sizeOfDrink == 'small':
    priceSize = 1.50
elif sizeOfDrink == 'medium':
    priceSize = 2.50
else:
    priceSize = 3.25

if flavorInDrink == 'vanilla' or flavorInDrink == 'lemon':
    priceFlavour = 0.25
elif flavorInDrink == 'maple' or flavorInDrink == 'mint':
    priceFlavour = 0.5
elif flavorInDrink == 'chocolate':
    priceFlavour = 0.75
else:
    priceFlavour = 0.0

#Calculate cost and net cost
cost = priceSize + priceFlavour
netCost = cost * TAX

#Display output
print("For", nameOfCustomer[0].upper()+nameOfCustomer[1:].lower() + ", a", sizeOfDrink, typeOfBeverage, ", with", flavorInDrink + ",cost: $ %.2f" % netCost)
