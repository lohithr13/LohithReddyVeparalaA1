""" pseudocode for two functions

    def Loading_items():
        display Hello, welcome to shopping List made by Lohith Reddy Veparala

        get_user_input = "please enter S to see shopping list"
            if (get_user_input != s or S)
            prompt
            else get_user_input = items()

        def items():
            display (Fish fingers,12.95,2,r/Metal detector,42.5,3,r/Coffee beans,40.0,1,r)
            return Loading_items

        def completed_items()
            user_input = "please enter C to display completed items
            elif user_input != C or c
            prompt
            user_input = Complete_items()

            return completed_items
    def Complete_items()
             display (complete items)"""

#Lohith Reddy Veparala.
#This is the program for a shopping list that allows the User to see the required and completed items and add new items and mark any item as complete.
#The sorting of the items will be done according to the priority.The price of each items and total will be showed in each case.
#link for Git-hub version : https://github.com/lohithr13/LohithReddyVeparalaA1

from operator import itemgetter

name = input("Please enter your name: ")
print ("Hello, welcome to the shopping list " + name + "!")


#The following function prints the menu of to-do actions from which customer can choose from.
# The customer is provided with options such as Listing the required items, Listing of the completed items, Adding a new item, Marking an existing item as completed and Quit.

def print_menu():
    menu_str = """

        Choose one of the options from the list :

        R - List required items
        C - List completed items
        A - Add new item
        M - Mark an item as completed
        Q - Quit
                                        - Lohith Reddy Veparala. """

    print(menu_str)



def get_input(valid_input):

    user_input = input("=>>").lower()

    if user_input not in valid_input:
        user_input = input("=>>").lower()

    return user_input

#req_items basically sorts the the items on the list and their information into the format of  Count, Item name, Price followed by the Priority given to the item.
#In here, the total price of the items in the list is also calculated by adding the prices of the mentioned items after formatting their information and details into an order.
#If there are no items in the list, then it will print out no required items mentioned.
#If the number of items are not zero, then it will be printed out saying the total price will be the calculated total_price.

def req_items():
    list_items.sort(key=itemgetter(2,0))
    count = 0
    total_price = 0

    for i in list_items:
        if(i[3]== "r"):

            total_price += float(i[1])
            print(count,'.',    i[0],   '$',float(i[1]),    i[2])
            count +=1

    if count == 0:
        print("No required items mentioned")
    else:
        print("The total price will be $",(total_price))

#comp_items basically displays the items that are marked complete by the customer.
#This function shows up by displaying no items are completed if there are no items marked as complete.
#If the customer has marked one or more items as complete, then the total price of those items will be displayed as The total price will be total_price.

def comp_items():

    list_items.sort(key=itemgetter(2,0))
    count = 0
    total_price = 0
    for f in list_items:
        if(f[3] == "c"):
            total_price += float(f[1])
            print("Completed items are listed below with their respective name, price and the priority given : \nProduct number = {}. \nProduct name = {}\nPrice = ${}\nPriority = ({})\n".format(count, f[0], float(f[1]), f[2]))
            count += 1

    if count == 0:
        print("Oops! Looks like no items are completed. Please mark an item and check back again!")
    else:
        print("The total price will be $",(total_price))

#add_items lets the customer add an item onto the list by asking the customer to input the name of the item.
#This also checks for invalid inputs such as not accepting a blank item name or a space in the item name's place.
#Once a valid name is input, then comes the price input where the same error checking applies for a blank price or a space.
#After price, follows the priority where the user has to put in a number (either a 1 or a 2 or a 3).
#It is finally printed that the Item name, Price, and the priority are added to the shopping list in a format.

def add_items():
    l = []

    while True:
        item_name = str(input("Please enter a valid item's name: "))

        if  item_name =="" or item_name ==" ":
            print("Error! The item name cannot be and empty space or be left blank")
            continue

        else:
            l.append(item_name)
            break

    while True:
        try:
            item_price = int(input("please enter the price of the item : "))

        except ValueError:
            print("The input must be a number: ")
            continue

        if item_price < 50:
            print ("The price must atleast be $50")
            continue

        else:
            l.append(item_price)
            break

    while True:
        priority = input("Please enter the priority of the item: ")

        try:
           int(priority)

        except ValueError or priority not in ('1', '2', '3'):
            print("Invalid input. The priority of the item must be a number among 1 or 2 or a 3")
            continue

        else:
            l.append(priority)
            l.append("r")
            break

    print("{}, ${} (priority {}) added to the shopping list.".format(l[0], float(l[1]), l[2]))

    list_items.append(l)

#mark_comp allows the user to mark an existing item to be marked as complete. The customer is asked to input the number of the item that needs to be marked.
#Once the item is found in the required items list, it will be marked complete and displays The item was successfully marked as complete.
#Once it is displayed, then the respective item is added to the list of completed items (choice c) on the main menu(print_menu)

def mark_comp():
    req_items()

    x = []
    for item in list_items:
       if(item[3] == "r"):
            x.append(item)
    user_input= int(input("Enter the number of the item to be marked as complete: "))
    count = 0

    for item in x:
        if(count == user_input):
            print("{} was successfully marked as complete".format(item[0]))
            item[3] = "c"
        count += 1

        for item in x:
         if(item[3] == "c"):
            for each in list_items:
                if(each[0] == item[0]):
                    each[3] = "c"
                    break

#load_items basically loads and connects the list of items from an external file to the present program.
#In this case the external file that has a list of required items is items.txt will will be imported and connected to the main program

def items_file():

    file_items = open("items.txt", "r")

    for each in file_items:
        list_items.append(each.replace("\n", "").split(","))

    file_items.close()

list_items = []
items_file()

#The customer is given a choice of Listing the required items, Listing of the completed items, Adding a new item, Marking an existing item as completed and Quit.
#When the customer choses the option q , then its is printed that All of the items have been saved to the external file items.txt.
#whereas, when any other choice from the menu is chosen then respective assigned functions are performed.
#For different options, different fucntions are performed such as for r = Listing the required items, c = Listing of the completed items, a = Adding a new item, m = Marking an existing item as completed and q = Quit.

while True:
    print_menu()
    customer_choice = get_input(["r", "c", "a", "m", "q"])

    if customer_choice == "q":
        print(" All of the items have been saved as you have chosen. Thank you! Have a great day! ")
        break

    elif customer_choice == "r":
        req_items()

    elif customer_choice == "c":
        comp_items()

    elif customer_choice == "a":
        add_items()

    elif customer_choice == "m":
        mark_comp()
