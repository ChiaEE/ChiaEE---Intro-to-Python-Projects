##Original Store inventory
Inventory= {"Milk": 3.15,"Cookies":2.12,"Eggs":3.78,"Tortillas":3.25,"Chicken Nuggets":5.25,"Muffins":3.65}

## The User Input
IBought= " "

##The Total Function
def Total(WholeCart,StoreInvent):
    '''The Prices Function takes the user's grocery list and the inventory as the parameters
    In the Nested Loop, the function iterates through the dictionary.
    If an item in the list is equal to a key in the dictionary, the value of the key is appended to the valuesSum list
    The Total variable is equal to the sum of the items in the valuesSum list''' 
    valuesSum = []
    for item in WholeCart:
        for key,value in StoreInvent.items():
            if key == item:
                valuesSum.append(value)               
    Total = sum(valuesSum)
    return Total

##The MyList Function
def MyList(Self,TheList,StoreInvent):
    ''' The MyList Function makes sure that ONLY what the user types from the inventory is added to their list
    this would prevent any mispellings of inventory items, capitilization issues, and avoids adding items that are not in the inventory
    The StoreInvent Parameter is the inital dictionary that represents the Inventory
    If the user's input is identical to a key/item in the dictionary/Inventory then the key is appended to their Shopping list
    The Self Parameter is the user input where they chose the items they want in their cart
    TheList Parameter represents the ShoppingList list'''
    for key,value in StoreInvent.items():
        if Self == key:
            TheList.append(key)
    return TheList
    


##Greeting Message
print("Welcome To The Grocery Store!" '\n')
##The inventory being shown to the user
print("Please see our Inventory:",Inventory, '\n')

##Creation of Shopping List
ShoppingList = []

##The while loop##
##if the user does not type the word 'stop',the loop continues
##The CorrectList variable calls the MyList Function. The IBought user input variable, ShoppingList list and Inventory Dictionary are the arguments.
##The user input is appended to the list through the CorrectList function call
##When the user types 'stop', the user's grocery list is printed.
##the CheckOut variable calls the Total function which uses the ShoppingList list and Inventory Dictionary as arguments
##The Total of all the items is printed as well as the user's list
while (IBought!= "stop"):
    IBought= input("What Would You Like In Your List? Type 'stop' when finished." '\n')
    if IBought == "stop":
        print("Your list :", ShoppingList)
        CheckOut = Total(ShoppingList,Inventory)
        print("Your Total Will Be :",CheckOut)
    else:
        CorrectList = MyList(IBought,ShoppingList,Inventory)
        
        

    
       
