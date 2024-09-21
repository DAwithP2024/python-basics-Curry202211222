# Products available in the store by category
products = {
    "IT Products": [
        ("Laptop", 1000),
        ("Smartphone", 600),
        ("Headphones", 150),
        ("Keyboard", 50),
        ("Monitor", 300),
        ("Mouse", 25),
        ("Printer", 120),
        ("USB Drive", 15)
    ],
    "Electronics": [
        ("Smart TV", 800),
        ("Bluetooth Speaker", 120),
        ("Camera", 500),
        ("Smartwatch", 200),
        ("Home Theater", 700),
        ("Gaming Console", 450)
    ],
    "Groceries": [
        ("Milk", 2),
        ("Bread", 1.5),
        ("Eggs", 3),
        ("Rice", 10),
        ("Chicken", 12),
        ("Fruits", 6),
        ("Vegetables", 5),
        ("Snacks", 8)
    ]
}

# Function to display sorted products based on name or price
def display_sorted_products(products_list, sort_order="name"):
    if sort_order == "name":
        products_list.sort(key=lambda x: x[0])
    elif sort_order == "price":
        products_list.sort(key=lambda x: x[1])
    for product in products_list:
        print(f"{product[0]} - ${product[1]}")

# Function to display all products by category
def display_products(products_dict):
    for category, items in products_dict.items():
        print(f"\n{category}:")
        for product, price in items:
            print(f"{product} - ${price}")

# Function to display available categories
def display_categories(products_dict):
    print("\nAvailable categories:")
    for category in products_dict:
        print(category)

# Function to add items to cart
def add_to_cart(cart, product, quantity):
    if product in cart:
        cart[product] += quantity
    else:
        cart[product] = quantity
    print(f"Added {quantity} of {product} to cart.")

# Function to display the cart
def display_cart(cart):
    print("\nYour cart:")
    total_cost = 0
    for product, quantity in cart.items():
        price = None
        # Searching the price in all categories
        for category in products.values():
            for item in category:
                if item[0] == product:
                    price = item[1]
                    break
        if price is not None:
            item_total = price * quantity
            total_cost += item_total
            print(f"{product} (x{quantity}) - ${item_total}")
    print(f"Total cost: ${total_cost}")

# Function to generate receipt
def generate_receipt(name, email, cart, total_cost, address):
    print("\nReceipt:")
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Shipping Address: {address}")
    print("\nPurchased Items:")
    for product, quantity in cart.items():
        print(f"{product} - Quantity: {quantity}")
    print(f"\nTotal cost: ${total_cost}")

# Function to validate name
def validate_name(name):
    parts = name.split()
    return len(parts) == 2 and all(part.isalpha() for part in parts)
# Function to validate email
def validate_email(email):
    return "@" in email and "." in email.split("@")[1]

# Main function to simulate a shopping experience
def main():
    cart = {}
    while True:
        print("\nOptions:")
        print("1. Display Categories")
        print("2. Display Products")
        print("3. Display Sorted Products by Name")
        print("4. Display Sorted Products by Price")
        print("5. Add to Cart")
        print("6. Display Cart")
        print("7. Checkout")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_categories(products)
        elif choice == "2":
            display_products(products)
        elif choice == "3":
            for category, items in products.items():
                print(f"\n{category}:")
                display_sorted_products(items, "name")
        elif choice == "4":
            for category, items in products.items():
                print(f"\n{category}:")
                display_sorted_products(items, "price")
        elif choice == "5":
            product_name = input("Enter the product name: ")
            quantity = int(input("Enter the quantity: "))
            # Check if the product exists
            for category in products.values():
                for item in category:
                    if item[0] == product_name:
                        add_to_cart(cart, product_name, quantity)
                        break
        elif choice == "6":
            display_cart(cart)
        elif choice == "7":
            name = input("Enter your name: ")
            if not validate_name(name):
                print("Invalid name.")
                continue
            email = input("Enter your email: ")
            if not validate_email(email):
                print("Invalid email.")
                continue
            address = input("Enter your shipping address: ")
            total_cost = sum(quantity * item[1] for product, quantity in cart.items()
                             for category in products.values() for item in category if item[0] == product)
            generate_receipt(name, email, cart, total_cost, address)
            break
        elif choice == "8":
            print("Exiting the store.")
            break
        else:
            print("Invalid choice, please try again.")

# Ensure the main() function is called when the program is run
if __name__ == "__main__":
    main()
