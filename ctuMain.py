import sys
from ctuClass import ctuStock                #Imported class from ctuClass

#Declare Variables for 4 difffrent shops
stock1 = ctuStock("default", "default", 0, 0, 0)
stock2 = ctuStock("default", "default", 0, 0, 0)
stock3 = ctuStock("default", "default", 0, 0, 0)
stock4 = ctuStock("default", "default", 0, 0, 0)
#The functions that displays my menu's
laptopstock = 50
computerstock = 50
hardwrestock = 50
textbookstock = 50


stockdict = {"Laptops":{"Price":"10 000","STOCK": laptopstock},"Computer Parts" : {"Price" : "3500", "STOCK":computerstock},
             "Hardware Parts" : {"Price":"5500", "STOCK":hardwrestock},"Study Textbooks":{"Price" : "3500", "STOCK" : textbookstock}}

def mainmenu():
    print("-----------------------------\nWelcome to CTU Technologies\n-----------------------------\n"
          "1.  Shop management\n2.  Sales\n3.  Returns\n4.  Stock\n99. Exit\n"
          "-----------------------------")
    option1 = (input("Select an option: "))
    if option1 == "1":
        shopmanage()
    if option1 == "2":
        sales()
    if option1 == "3":
        returns()
    if option1 == "4":
        stock()
    if option1 == "99":
        sys.exit()
    else:
        mainmenu()


#the IF Statements for the first menu of the preogram

def shopmanage():
    print("-----------------------------\nShop Management\n-----------------------------")
    print("1. Change Shop Name\n2. Change Shop Location\n3. Display Current Shops\n4. Display all Shops Information"
          "\n0. Back\n")
    option2 = (input("Select an Option: "))
    if option2 == "1":
        changeshopname()
    if option2 == "2":
        changeshoplocal()
    if option2 == "3":
        dispcurrshops()
    if option2 == "4":
        dispallshops()
    if option2 == "0":
        mainmenu()
#this function is used to create the shop management tab in the program

def changeshopname():
    print("-----------------------------\nChange Shop Name\n-----------------------------")
    print("1.", stock1.shopName, "\n2.", stock2.shopName, "\n3.", stock3.shopName, "\n4.", stock4.shopName, )
    option3 = (input("\nSelect an Option: "))
    if option3 == "1":
        newshopnam = input("New Shop Name?:")
        if newshopnam.strip() == '':
            print("\nENTER A VALID NAME\n")
            changeshopname()

        stock1.shopName = newshopnam
        print("Shop name succecfully changed to", stock1.shopName)



    elif option3 == "2":
        newshopnam1 = input("New Shop Name?:")
        if newshopnam1.strip() == '':
            print("\nENTER A VALID NAME\n")
            changeshopname()
        stock2.shopName = newshopnam1
        print("Shop name succecfully changed to", stock2.shopName)
    elif option3 == "3":
        newshopnam2 = input("New Shop Name?:")
        if newshopnam2.strip() == '':
            print("\nENTER A VALID NAME\n")
            changeshopname()
        stock3.shopName = newshopnam2
        print("Shop name succecfully changed to", stock3.shopName)
    elif option3 == "4":
        newshopnam3 = input("New Shop Name?:")
        if newshopnam3.strip() == '':
            print("\nENTER A VALID NAME\n")
            changeshopname()
        stock4.shopName = newshopnam3
        print("Shop name succecfully changed to", stock4.shopName)
    else:
        print("\nInvalid input, Select a Valid option\n")
        shopmanage()
#this function prints the change shop name tab and gives you the option to change it.

def changeshoplocal():
    print("-----------------------------\nChange Shop Location\n-----------------------------")
    print("1.", stock1.shopName, ",", stock1.shopLocation, "\n2.", stock2.shopName, ",", stock2.shopLocation, "\n3.",
          stock3.shopName, ",", stock3.shopLocation, "\n4.", stock4.shopName, ",", stock4.shopLocation)
    option4 = (input("\nSelect an Option:"))
    if option4 == "1":
        newshoplocal = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal == "KZN" or newshoplocal == "Free State" or newshoplocal == "Gauteng" or\
                newshoplocal == "Limpopo" or newshoplocal == "Default":
            stock1.shopLocation = newshoplocal
            print("Shop Location has officially been changed to", stock1.shopLocation)
        else:
            print("Invalid Location")
    elif option4 == "2":
        newshoplocal1 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal1 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock2.shopLocation = newshoplocal1
            print("Shop Location has officially been changed to", stock2.shopLocation)
        else:
            print("Invalid Location")
            shopmanage()
    elif option4 == "3":
        newshoplocal2 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal2 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock3.shopLocation = newshoplocal2
            print("Shop Location has officially been changed to", stock3.shopLocation)
        else:
            print("Invalid Location")
    elif option4 == "4":
        newshoplocal3 = input("New Shop Location?: KZN/Free State/Gauteng/Limpopo/Default/\n")
        if newshoplocal3 == "KZN" or "Free State" or "Gauteng" or "Limpopo" or "Default":
            stock4.shopLocation = newshoplocal3
            print("Shop Location has officially been changed to", stock4.shopLocation)
        else:
            print("Invalid Location")
#this function changes the location but also prints the name in the change shop location tab

def dispcurrshops():
    print("-----------------------------\nCurrent shop available\n-----------------------------")
    print("1. ",stock1.shopName, ",", stock1.shopLocation, "\n2. ", stock2.shopName, ",", stock2.shopLocation,
          "\n3. ", stock3.shopName, ",", stock3.shopLocation,"\n4. ", stock4.shopName, ",", stock4.shopLocation)
#this function displays all the current by name and location

def dispallshops():
    print("-----------------------------\nAll shops info\n-----------------------------\n\n")
    print("------------------------\nShop Name: ",stock1.shopName,"\nShopLocation: ",stock1.shopLocation,
          "\nNumber of Customers: ",stock1.customers,"\nCurrent Sales: ",stock1.sales,"\nReturns: ",stock1.returns)
    print("------------------------\nShop Name: ", stock2.shopName, "\nShopLocation: ", stock2.shopLocation,
          "\nNumber of Customers: ", stock2.customers, "\nCurrent Sales: ", stock2.sales, "\nReturns: ", stock2.returns)
    print("------------------------\nShop Name: ", stock3.shopName, "\nShopLocation: ", stock3.shopLocation,
          "\nNumber of Customers: ", stock3.customers, "\nCurrent Sales: ", stock3.sales, "\nReturns: ", stock3.returns)
    print("------------------------\nShop Name: ", stock4.shopName, "\nShopLocation: ", stock4.shopLocation,
          "\nNumber of Customers: ", stock4.customers, "\nCurrent Sales: ", stock4.sales, "\nReturns: ", stock4.returns,
          "\n------------------------")
#this function displays all shops info

def sales():
    print("\n-----------------------------\nSales\n-----------------------------\n")
    item = (input("Select an item you want to buy:\n1. Laptops\n2. Computer Parts\n3. Hardware Parts\n"
                     "4. Study Textbooks"))
    ammount = int(input("How much of these items do you need."))
    print("1. ", stock1.shopName, "\n2. ", stock2.shopName, "\n3. ", stock3.shopName, "\n4. ", stock4.shopName)
    shop = (input("What shop do you want the item to be shipped from"))


    if item == "1":
        stockdict['Laptops']['STOCK'] -= ammount
        print("Your", ammount, "Laptops will be shipped to the chosen store.")
    elif item == "2":
        stockdict['Computer Parts']['STOCK'] -= ammount
        print("Your", ammount, "Computer Parts will be shipped to the chosen store store.")
    elif item == "3":
        stockdict['Hardware Parts']['STOCK'] -= ammount
        print("Your", ammount, "Hardware Parts will be shipped to the chosen store.")
    elif item == "4":
        stockdict['Laptops']['STOCK'] -= ammount
        print("Your", ammount, "Study Textbooks will be shipped to the chosen store.")
    else:
        print("invalid")
########################################################################################################################
########################################################################################################################
    if shop == "1":
        stock1.customers += 1
        stock1.sales += ammount             #2 Diffrent if statements in the method, to increment the sales as well as the customer ammount
    elif shop == "2":                         # I used the hashes to seperate the 2 if statements, to make it more readable
        stock2.customers += 1
        stock2.sales += ammount
    elif shop == "3":
        stock3.customers += 1
        stock3.sales += ammount
    elif shop == "4":
        stock4.customers += 1
        stock4.sales += ammount
    else:
        print("Invalid")

#this function is used to create the sales tab
def returns():
    print("\n-----------------------------\nReturns\n-----------------------------\n")
    print("1.", stock1.shopName, "\n2.", stock2.shopName, "\n3.", stock3.shopName, "\n4.", stock4.shopName, )
    retlocal = input("What shop did you buy this item from?")
    print("What item do you want to return?\n\n1. Laptops\n2. Computer Parts\n3. Hardware Parts\n"
                     "4. Study Textbooks\n")
    retitem = input("Which one of these items do you want to return?")
    totretitem = int(input("How many items do you want to return?"))

    if retitem == "1":
        print("Your Laptops will be returned to the chosen store ")
    elif retitem == "2":
        print("Your Computer Parts will be returned to the chosen store ")
    elif retitem == "3":
        print("Your Hardware Parts will be returned to the chosen store ")
    elif retitem == "4":
        print("Your Study text books will be returned to the chosen store ")
########################################################################################################################
########################################################################################################################
    if retlocal == "1":
        stock1.returns += totretitem
        stock1.sales -= 1
    elif retlocal == "2":
        stock2.returns += totretitem
        stock2.sales -= 1
    elif retlocal == "3":
        stock3.returns += totretitem
        stock3.sales -= 1
    elif retlocal == "4":
        stock4.returns += totretitem
        stock4.sales -= 1
#this function was made to create and use the return tab

def stockprint():
    for key, value in stockdict.items():
        print(key, '')
        for category, amount in value.items():
            print(category, ':', str(amount))
#this function is used to print the stock in the specific way
def addstock():
    newproduc = input("Select an Product to add stock:\n\n1. Laptops\n2. Computer Parts\n3. Hardware Parts\n4. Study Textbooks")
    if newproduc == "1":
        print("You have selected laptops")
        stockaddtot = int(input("How much stock do you want to add?"))
        stockdict["Laptops"]["STOCK"] += stockaddtot
    elif newproduc == "2":
        print("You have selected computer parts")
        stockaddtot = int(input("How much stock do you want to add?"))
        stockdict["Computer Parts"]["STOCK"] += stockaddtot
    elif newproduc == "3":
        print("You have selected computer parts")
        stockaddtot = int(input("How much stock do you want to add?"))
        stockdict["Hardware Parts"]["STOCK"] += stockaddtot
    elif newproduc == "4":
        print("You have selected computer parts")
        stockaddtot = int(input("How much stock do you want to add?"))
        stockdict["Study Textbooks"]["STOCK"] += stockaddtot

    print("Price and stock added successfully!")

    stockprint()
#this function used to give the user a choice to add a new function

def stock():
    print("\n-----------------------------\nStock\n-----------------------------\n")
    print("1. Display stock\n2. Add stock\n0. Back")
    stockop = input("Choose an option: ")
    if stockop == "1":
        stockprint()
    elif stockop == "2":
        addstock()
#This code is used to create the stock tab in the main menu

while True:
    mainmenu()
    input("\nPress ENTER to return to Main Menu")
#My main loop I am done