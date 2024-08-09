# Updated products dictionary with quantity and cost
from random import choice


products = {
    "1": {"chocolate": {"quantity": 50, "cost": 20}},
    "2": {"Juice": {"quantity": 100, "cost": 10}},
    "3": {"Cola": {"quantity": 250, "cost": 15}},
    "4": {"Goodies": {"quantity": 100, "cost": 25}},
}


# resources = {
#     "chocolate": 10,
#     "Juice": 5,  
#     "Cola": 10,
#     "Goodies": 8
# }


profit = 0

def check_report():
    """Check the product quantity report."""
    print(f"Chocolate: {products['1']['chocolate']['quantity']} pieces available.")
    print(f"Juice: {products['2']['Juice']['quantity']} pieces available.")
    print(f"Cola: {products['3']['Cola']['quantity']} pieces available.")
    print(f"Goodies: {products['4']['Goodies']['quantity']} pieces available.")
    
def resource_sufficient(order_product, user_choice):
    """Check if resources are sufficient for the order."""
    for item, details in order_product.items():
        if details['quantity'] > products[user_choice][item]['quantity']:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def payment_process():
    """Handle payment processing."""
    payment_choice = input("How do you want to pay: card or cash? ").lower()
    if payment_choice == 'card':
        print("Thank you for the payment.")
        return float('inf') 
    elif payment_choice == 'cash':
        print("Please insert the coins.")
        total = int(input("How many 1sek coins? ")) * 1
        total += int(input("How many 2sek coins? ")) * 2
        total += int(input("How many 5sek coins? ")) * 5
        return total
    else:
        print("Invalid payment method.")
        return 0
    

def process_order(user_choice):
    """Process the user's order."""
    global profit
    order = products[user_choice]
    product_name, details = list(order.items())[0]
    quantity_needed = 1  
    price = details['cost']
    
    # Create a new order product dictionary
    order_product = {product_name: {'quantity': quantity_needed}}

    # Check if resources are sufficient
    if resource_sufficient(order_product, user_choice):
        payment = payment_process()
        
        # Check if payment is sufficient
        if payment >= price:
            change = round(payment - price, 2)
            products[user_choice][product_name]['quantity']  -= quantity_needed  # Decrease resource count after successful purchase
            profit += price  # Update global profit
            print(f"Transaction successful. You selected {product_name} with a price of {price}sek. Your change is {change}sek.")
            return change
        else:
            print("Sorry, that's not enough money. Money refunded.")
            return None
    else:
        print("Sorry, resources are not sufficient.")
        return None

def vending_machine():
    """Main function to run the vending machine."""
    user_choice = input("Press the number button for: 1. Chocolate 2. Juice 3. Cola 4. Goodies or type 'report' to check the report: ")
    print()

    if user_choice == "report":
        check_report()
    elif user_choice in products:
        item = products[user_choice]
        product_name, details = list(item.items())[0]
        price = details['cost']
        print(f"You selected: {product_name} with a price of {price}sek")
        process_order(user_choice)
    else:
        print("Invalid selection.")

# Run the vending machine
vending_machine()
