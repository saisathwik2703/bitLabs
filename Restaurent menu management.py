import sys

# 1. At first add the items in the list (The Menu/Catalog)
CATALOG = {
    1: {'name': 'Pizza', 'price': 15.00},
    2: {'name': 'Burger', 'price': 12.50},
    3: {'name': 'Pasta', 'price': 18.00},
    4: {'name': 'Salad', 'price': 9.00},
    5: {'name': 'Tacos', 'price': 11.00},
}

def calculate_order_total(cart_items: dict, custom_discount_percent: float) -> float:
    """
    Calculates the final total price for the selected items after applying a custom discount.

    Args:
        cart_items: A dictionary where keys are selected item names and values are prices.
        custom_discount_percent: The discount to apply (e.g., 10.0 for 10%).

    Returns:
        The final total price after the discount.
    """
    if not cart_items:
        print("\nOrder is empty. Total price: $0.00")
        return 0.0

    # 2. Calculate the amount for selected items (Subtotal)
    subtotal = sum(cart_items.values())
    
    print(f"\n--- Order Calculation ---")
    print(f"Subtotal (Price of selected items): ${subtotal:,.2f}")

    current_total = subtotal
    
    # 3. Add discount to that price
    if custom_discount_percent > 0:
        custom_discount_rate = custom_discount_percent / 100.0
        custom_discount_amount = current_total * custom_discount_rate
        current_total -= custom_discount_amount
        print(f"Discount Applied ({custom_discount_percent:.2f}%): -${custom_discount_amount:,.2f}")
    else:
        print("No Custom Discount applied.")

    # 4. Return the final total
    return current_total

def get_user_order(catalog: dict):
    """
    Displays the catalog and gathers user selections and discount percentage.
    """
    cart_items = {}
    
    # Display the list
    print("\n--- Restaurant Menu (Select by ID) ---")
    for item_id, item_info in catalog.items():
        print(f"[{item_id}] {item_info['name']:<15} - ${item_info['price']:,.2f}")
    print("---------------------------------------")

    try:
        # User should select items from the list
        selection_input = input(
            "Enter the IDs of the items you wish to order, separated by commas (e.g., 1, 3, 5): "
        ).strip()
        
        selected_ids = []
        if selection_input:
            selected_ids = [int(item_id.strip()) for item_id in selection_input.split(',')]

        # Build the cart based on valid selections
        for item_id in selected_ids:
            if item_id in catalog:
                item_info = catalog[item_id]
                # Using a list to allow multiple same items, but keeping it simple by only adding one of each here
                cart_items[item_info['name']] = catalog.get(item_id, {}).get('price', 0)
            else:
                print(f"Warning: Item ID {item_id} not found in menu and was skipped.")

        # Get the discount from the user
        custom_discount_percent = float(input("\nEnter the custom discount percentage to apply (e.g., 10 for 10%): "))
        if custom_discount_percent < 0:
            print("Discount must be non-negative. Setting to 0%.")
            custom_discount_percent = 0.0

    except ValueError:
        print("\nInvalid input detected. Please enter numbers for IDs/Discount.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

    return cart_items, custom_discount_percent

# Main execution block
if __name__ == "__main__":
    print("Welcome to the Restaurant Menu Ordering System.")

    # 1. & 2. Display list and get user selection/discount
    user_cart_items, user_custom_discount = get_user_order(CATALOG)
    
    # Print selected items for confirmation
    if user_cart_items:
        print("\n--- Your Order ---")
        for name, price in user_cart_items.items():
            print(f"- {name}: ${price:,.2f}")
        print("------------------")
        
        # 3. & 4. Calculate and apply discount
        final_price = calculate_order_total(user_cart_items, user_custom_discount)

        # 5. Print the final price
        print("\n====================================")
        print(f"FINAL PRICE: ${final_price:,.2f}")
        print("====================================")
    else:
        print("\nNo items were selected for the order.")
