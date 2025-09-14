#Name: Arittri Ray
#ID: u3312851
#Date: 12 September 2025
#CaseStudy1

menu = {
    "coffee": (3.50, "drink"),
    "tea": (3.00, "drink"),
    "juice": (4.00, "drink"),
    "burger": (6.00, "food"),
    "nuggets": (5.50, "food"),
    "sandwich": (6.00, "food"),
    "cake": (8.00, "food")
}

def show_menu():    #Displays the menu
    print("\n")
    print("~~~~~~~~~~~~Café Menu~~~~~~~~~~~~")
    print("Item========Price=======Category")
    print("-"*33)
    for item, (price, category) in menu.items():
        print(f"{item.title(): <12}${price: <11.2f} {category.title()}")
    print("-"*33)

def add_item(cart): #Adds item to cart
    try:
        print("\n")
        item = input("Enter item name: ").lower()
        if item not in menu:
            print("Invalid Item")
        else:
            try:
                quantity = int(input("How many?: "))
                if quantity > 0:
                    price, category = menu[item]
                    cart.append((item, quantity, price, category))
                    print(f"{item.title()} x{quantity} added to cart")
                else:
                    print("Quantity can NOT be negative")
            except Exception as e:
                print("Invalid. \nPlease try again!", e)       #Handles any sort of exception raised
    except Exception as e:
        print("Invalid. \nPlease try again!", e)    #Handles any sort of exception raised

def view_cart(cart):    #Views Cart
    if not cart:
        print("Cart is empty")  #Shows Empty Cart
        return

    print("\n")
    print("="*14 + "Your Cart" + "="*17)
    print("Item" + "-"*8 + "Qty" + "-"*6 + "Price" + "-"*6 + "Category")
    print("="*40)
    for item, quantity, price, category in cart:
        print(f"{item.title():<12} {quantity:<7} {price*quantity:<11.2f} {category.title():<12}")

def checkout(cart):     #Prints Receipt
    if not cart:
        print("Cart is Empty")
        return

    subtotal = 0
    categories = set()

    print("\n")
    print("=" * 23 + "Receipt" + "=" * 30)
    for item, quantity, price, category in cart:    #displays line total
        line_total = price*quantity
        subtotal += line_total
        categories.add(category)
        print(f"{item: <10} x{quantity: <8} - Price: ${price: <8.2f} = Line total: {line_total: <10.2f}")

    tax = 0.10
    tax_amount = subtotal * tax
    total = subtotal + tax_amount

    while True:
        student = input("Are you a student? Y/N: ").lower()

        if student in ('y', 'n'):       #input validation
            break
        print("Please type: Y/N")

    discount1 = False
    discount2 = False

    if student == "y":          #student discount
        student_discount = 0.05
        total -= (total*student_discount)
        discount1 = True
        print("\n")
        print("You got a 5% student discount!")

    if "food" in categories and "drink" in categories:          #meal deal discount
        total -= 2.00
        discount2 = True
        print("You got a $2.00 meal-deal (food + drink) discount!")

    print("\n")
    print("Categories of items: ", ",".join(categories).title())        #displays the categories of the food ordered

    print(f"Subtotal : {subtotal: .2f}" )
    print(f"Tax : 10%")
    print(f"Tax_amount : {tax_amount: .2f}")
    if discount1:
        print("Student Discount: 5%")
    if discount2:
        print("Meal-Deal discount: $2.00")
    print(f"Total: {total: .2f}")
    cart.clear()

def main():
    cart = []
    while True:
        print("\n")
        print("="*15 + "Café Console" + "="*15)
        print("\n1. Show Menu\n2. Add Item\n3. View Cart\n4. Checkout\n5. Exit")
        choice = input("Choose an option: ")


        if choice == "1":
            show_menu()
        elif choice == "2":
            add_item(cart)
        elif choice == "3":
            view_cart(cart)
        elif choice == "4":
            checkout(cart)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid. \nPlease try again.")

if __name__ == "__main__":
    main()















