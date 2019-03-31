items = []


def addItem(price,name):
    items.append([name,price])

def displayMenu():
    global items
    print("Here's the menu for today:\n")
    print("ITEM_CODE\tITEM_NAME\t\t\tITEM_PRICE")
    for n in range(0,len(items)):
        print(str(n+1)+".\t\t\t"+str(items[n][0])+"\t\t₹"+str(items[n][1]))

def calculatePrice(code):
    global items
    ordered_items=[]
    for item in code:
        ordered_items.append(int(item))

    sum=0
    for item in ordered_items:
        try:
            sum+=items[item-1][1]
        except IndexError:
            while(True):
                print("The item numbers you have entered are not available")
                print("Please enter valid item numbers")
                choice = input("Do you want to order again? (Y/N)")
                if (choice == "N" or choice == "n"):
                    exit()
                else:
                    finalOrderMenu()


    return sum

def displayOrder(code):
    global items
    print("BREAK DOWN OF YOUR ORDER:\n")
    print("ITEM_CODE\tITEM_NAME\tITEM_PRICE\nQUANTITY_ORDERED\tTOTAL_PRICE")
    ordered_items = []
    processed_items = ordered_items
    for item in code:
        ordered_items.append(int(item))
    for i in range(0,len(items)):

        quantity = 0
        price = 0
        for j in range(0,len(processed_items)):
            if(processed_items[j]==i+1):
                quantity+=1
                price+=items[i][1]



        if (quantity > 0):
            processed_items = [y for y in processed_items if y != i + 1]
            print(str(i + 1) + ".\t" + str(items[i][1]) + "\t" + str(items[i][0]) + "\t" + str(
                quantity) + "\t₹" + str(price))


addItem(10,"Samosa         ")
addItem(15,"Aloo Tikki     ")
addItem(35,"Bun Samosa     ")
addItem(30,"Oreo Milkshake ")
addItem(15,"Fresh Lime Soda")

def finalOrderMenu():
    while(True):
        print("Welcome to our store.\n")
        displayMenu()
        order=input("What would you like to order today? ")
        calculatePrice(order)
        displayOrder(order)
        print()
        print("Your  final bill amount is Rs."+str(calculatePrice(order)))
        print()
        choice=input("Do you want to order again? (Y/N)")
        if(choice=="N" or choice=="n"):
            print()
            print("==========================")
            print("Thank you for shopping with us.")
            break
        print()
        print("==========================")

finalOrderMenu()
