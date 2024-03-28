#importing libraries

from datetime import datetime
import time


#Defining functions

                                        #For saving user's data

def save_register(data):
    '''
    data will be the dictionary that will be created from choice=1 when user gives
    username, password, first name and last name.
    '''
    with open("Database.txt","a") as file:
        file.write(f"{data['username']},{data['password']},{data['first_name']},{data['last_name']}\n")


                                         #For loading database

user_data = []

def collection():
    with open("Database.txt","r") as file:
        line_by_line = file.readlines()
        for line in line_by_line:
            username,password,first_name,last_name = line.split(",")
            user_info = {'username':username,'password':password,'first_name':first_name,'last_name':last_name}
            user_data.append(user_info)
        return user_data


                            #Check if the user entered unique username or not
def taken_username():
    unique_un = collection()
    for check in unique_un:
        if check['username'] == username:
            return True


                                        #For logging in
                                        
def login():
    all_users_data = collection()
    for verify in all_users_data:
        if verify['username'] == username and verify['password'] == password:
            print("Login Successful!\n")
            # print(f"Welcome {first_name} {last_name}!")
            return True


                                         #Our Products
            
prods = {'Coffee Maker':2000, 'Stainless Steel Cooker':1500, 
        'Electric Kettle':2500, 'Juicer':1500, 'Pressure Cooker':1400,
        'Toaster Oven':3000, 'Tea Kettle':800, 'Meat Grinder':4000,
        'Popcorn Maker':1800, 'Bread Toaster':1000}


                                    #For Displaying Products

def display_products(prods):
    print("Available List of Products: ")
    for index,(product, price) in enumerate(prods.items() , start = 1):
        print(f"{index}. {product} - Rs {price}")


                                        #Adding to Cart
        
def add_to_cart(prods):
    display_products(prods)

    # try-except block is handling error if user enters non-int value
    try:
        item_index = int(input("Enter the item number you want to add: "))
        if 1<=item_index<=len(prods):
            product_list = list(prods.keys())
            add = product_list[item_index - 1]
            
            '''
            prods.keys is accessing all the product names, we typecasted it to list to access
            products through indexing.

            We are subtracting 1 from item_index because in python, indexing starts from 0 and we are
            showing it from 1.
            '''

            with open(f"{username}'s_cart.txt",'a') as file:
                file.write(f"{add}:{prods[add]} Rs\n")
                print(f'{add} added to cart!')

        # If user enters wrong item number
        else:
            print("Enter an existing item!")
    except ValueError:
        print("Invalid choice!")


                                       #Removing from cart

def remove_from_cart():
    # try-except block is used for checking if the file exists or not
    try:
        with open((f"{username}'s_cart.txt")) as file:
            cart_list = file.readlines()

    # Cart exists but empty.
        if not cart_list:
            print("Add something to cart first!")
            time.sleep(1)
            return

    # Cart have items
        cart = []
        for item in cart_list:
            cart.append(item)
        print("Current items in your cart: ")
        for index, item in enumerate(cart, start=1):
            print(f"{index}. {item}",end = "")
            # item contains both product and price

        while True:
            # try-except is used for handling error if user enters non-int
            try:
                remove_index = int(input("Enter the item number you want to remove: "))

                if remove_index < 1 or remove_index > len(cart):
                    print("Enter an existing item number.")

                else:
                    removed_item = cart.pop(remove_index - 1)
                    print(f"{removed_item}".strip('\n'),end = '')
                    print(" removed from cart!")

                more = input("Do you want to remove more items? Y/y or any other key to go back: ")
                if more.lower() == "y":
                    print("Updated items in your cart: ")
                    for index2, rem_item in enumerate(cart, start=1):
                        print(f"{index2}. {rem_item}",end = "")
                    continue
                else:
                    break
            except ValueError:
                print("Invalid item number!")

        # Opening file in "w" mode to erase existing cart and write the new(removed) cart.
        with open(f"{username}'s_cart.txt","w") as file:
            for item2 in cart:
                file.write(f"{item2}")
    except FileNotFoundError:
        print("Add something to cart first!")
        time.sleep(1)


                                         # For Viewing Cart

def view_cart():
    #try-except block is handling error if file exists or not.
    try:
        with open((f"{username}'s_cart.txt")) as file:
            cart_view = file.readlines()

        #Cart is not empty
        if cart_view:
            cart2 = [item2 for item2 in cart_view]
            
            print("Current items in your cart: ")
            for index2, item2 in enumerate(cart2, start=1):
                print(f"{index2}. {item2}",end = "")
            return True

        #Cart exists but empty
        else:
            print("Cart is empty. Add something to cart first!")
            return False
        
        #Cart does not exist, but we are printing the same message
    except FileNotFoundError:
        print("Cart is empty. Add something to cart first!")


                                    # For viewing Shopping History
        
def shopping_history():
    # try-except block is handling error if file exists or not.
    try:
        with open(f"{username}'s_history.txt","r") as shop_hist:
            hist_list = shop_hist.readlines()
            for show_hist in hist_list:
                print(show_hist , end = '')
            return True
    except FileNotFoundError:
        print("Shop something to view your history!")


                                        # For checkout
        
def checkout():
    # try-except block is handling error if user's cart file exists or not.
    try:
        with open((f"{username}'s_cart.txt")) as file:
            bill = 0
            cart_check = file.readlines()
    
            # Cart exists but is empty
            if not cart_check:
                print("Your cart is empty. Add items before checkout.")
                time.sleep(1)
                return

            # Cart exists and have items
            print("Items in your cart: ") 
            for final_items in cart_check:
                print(final_items, end='')

            for total in cart_check:
                items2,prices2 = total.split(":")
                bill+=int(prices2.replace(" Rs\n",""))
            print("Total bill is Rs",bill)


            final = input("Press Y/y to confirm or any other key to go back: ")
            if final.lower() == "y":
                with open(f"{username}'s_history.txt","a") as hist_file:
                    hist_file.write(f"Date & Time: {time.ctime()}\n")
                    for history in cart_check:
                        hist_file.write(history)
                    hist_file.write(f"Bill: Rs {bill}\n\n")
                    

                with open(f"{username}'s_cart.txt","w") as clear_file:
                    print("Checkout Successful!\nThankyou for Shopping with us!")
                    return True
            else:
                print("Checkout Cancelled!")
                return False
            
    except FileNotFoundError:
        print("Add something to cart first!")
        time.sleep(1)


                                            #*****Actual Program*****
        
# try-except block is handling Keboard Interruption
try:
    while True:
        print("********** Welcome to Crockery Store**********")
        time.sleep(1)
        print("1. Register your account\n2. Login to an existing account")

        # try-except block is handling if user enters non-int
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                while True:
                    username = input("Enter your username: ")

                    '''
                    Checks for ensuring that user has entered username that is not empty,
                    has no capital characters, contains both alphabets and numbers, and is unique.
                    '''

                    if username.strip() == '':
                        print("Username cannot be empty!")

                    elif " " in username:
                        print("Username cannot have spaces!")

                    elif any(check3.isupper() for check3 in username):
                        print("Username cannot have upper case characters!")

                    elif not any(check4.isdigit() for check4 in username):
                        print("Username must contain atleast one number!")

                    elif not any(check5.isalpha() for check5 in username):
                        print("Username must contain atleast one alphabet!")

                    elif taken_username():
                        print("Username already taken. Try another username!")
                        
                    else:
                        while True:
                            password = input("Enter your password (minimum 6 characters): ")
                            if len(password) >= 6:
                                if not password.strip():
                                    print("Password cannot be empty or all spaces!")
                                else:
                                    break  # Exits the loop if a valid password is provided
                            else:
                                print("Password must be of minimum 6 characters!")

                        while True:
                            first_name = input("Enter your First Name: ")
                            if not first_name.strip():
                                print("First Name cannot be empty!")
                            elif " " in first_name:
                                print("First Name cannot have spaces!")
                            else:
                                break  # Exits the loop if a valid first name is provided

                        while True:
                            last_name = input("Enter your Last Name: ")
                            if not last_name.strip():
                                print("Last Name cannot be empty!")
                            elif " " in last_name:
                                print("Last Name cannot have spaces!")
                            else:
                                break  # Exits the loop if a valid last name is provided

                        # Then saves all fields in a dictionary
                        data = {"username": username, "password": password, "first_name": first_name, "last_name": last_name}
                        save_register(data)
                        print("User Registered Successfully. Now you can login!")
                        break
            elif choice == 2:
                username = input("Enter your username: ")
                password = input("Enter your password: ")
                if login():
                    time.sleep(1)
                    while True:
                        print("1. View product list\n2. Add items to cart\n3. Remove items from cart\n4. View cart\n5. View shopping history\n6. Checkout")
                        choice2 = input('Enter choice number [Q/q to quit]: ')
                        if choice2 == '1':
                            while True:
                                display_products(prods)
                                option = input("Press any key to go back: ")
                                break

                                
                        elif choice2 == '2':
                            while True:
                                add_to_cart(prods)
                                cont = input("Do you want to add more items? Y/y or press any key to go back : ")
                                if cont.lower() == "y":
                                    continue
                                else:
                                    break


                        elif choice2 == '3':
                            remove_from_cart()
                           

                        elif choice2 == '4':
                            view_cart()
                            while True:
                                opt3 = input("Press any key to go back: ")
                                break


                        elif choice2 == '5':
                            shopping_history()
                            while True:
                                choice3 = input("Press any key to go back: ")          
                                break


                        elif choice2 == '6':
                            checkout_successful = checkout()
                            if checkout_successful:
                                quit()


                        elif choice2.lower() == 'q':
                            print("Exiting the program!")
                            quit()
                            

                        else:
                            print("Invalid choice!")


                elif not login():
                    print('Invalid username or password!')


            else:
                print("Invalid choice!")

        except ValueError:
            print("Invalid Choice!")
            time.sleep(1)


except KeyboardInterrupt:
    print("Keyboard interruption! Exiting the program!")
