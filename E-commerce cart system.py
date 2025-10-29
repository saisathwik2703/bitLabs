import sys

# Global Catalog: Define the available products and their prices
CATALOG = {
    1: {'name': 'Laptop', 'price': 70000},
    2: {'name': 'Mobile Phone', 'price': 50000},
    3: {'name': 'Headphones', 'price': 2000},
    4: {'name': 'Mouse', 'price': 1000},
    5: {'name': 'Keyboard', 'price': 1500},
    6: {'name': 'Monitor', 'price': 15000},
    7: {'name': 'Webcam', 'price': 800},
    8: {'name': 'Gaming Chair', 'price': 10000},
}

def calculate_cart_total(cart_items: dict, custom_discount_percent: float) -> float:
    """
    Calculates the total price of the selected items in the cart, applying
    cascading discounts.

    Args:
        cart_items: A dictionary where keys are item names and values are prices
                    (only for selected items).
        custom_discount_percent: The additional discount to apply (e.g., 5.0 for 5%).

    Returns:
        The final total price after all applicable discounts.
    """
    # 1. Handle empty cart
    if not cart_items:
        print("\nCart is empty. Total price: 0.00")
        return 0.0

    # 2. Calculate the initial subtotal
    subtotal = sum(cart_items.values())
    num_items = len(cart_items)

    print(f"\n--- Calculation Summary ---")
    print(f"Total *selected* items in cart: {num_items}")
    print(f"Initial Subtotal: ${subtotal:,.2f}")

    current_total = subtotal
    total_discounts = 0.0

    # 3. Apply custom discount (Applied first)
    print("\n--- Step 1: Apply Custom Discount ---")
    if custom_discount_percent > 0:
        custom_discount_rate = custom_discount_percent / 100.0
        custom_discount_amount = current_total * custom_discount_rate
        current_total -= custom_discount_amount
        total_discounts += custom_discount_amount
        print(f"Custom Discount ({custom_discount_percent:.2f}%): -${custom_discount_amount:,.2f}")
        print(f"Total Price After Custom Discount: ${current_total:,.2f}")
    else:
        print("No Custom Discount applied.")
        print(f"Current Price: ${current_total:,.2f}")

    # 4. Check and apply 10% volume discount (if item count > 5) - Applied second/last
    print("\n--- Step 2: Apply Volume Discount ---")
    VOLUME_DISCOUNT_RATE = 0.10
    if num_items > 5:
        volume_discount = current_total * VOLUME_DISCOUNT_RATE
        current_total -= volume_discount
        total_discounts += volume_discount
        print(f"Volume Discount (10% off for > 5 items): -${volume_discount:,.2f}")
        print(f"Total Price After Volume Discount: ${current_total:,.2f}")
    else:
        print("No Volume Discount applied (Less than 6 items).")
        print(f"Current Price: ${current_total:,.2f}")

    # 5. Return the final total
    print("\n--- Final Summary ---")
    print(f"Total Savings Across All Discounts: ${total_discounts:,.2f}")
    return current_total

def get_user_input(catalog: dict):
    """
    Displays the catalog and gathers user selections and discount percentage.
    """
    cart_items = {}
    
    print("\n--- Available Products ---")
    for item_id, item_info in catalog.items():
        print(f"[{item_id}] {item_info['name']:<15} - ${item_info['price']:,.2f}")
    print("--------------------------")

    try:
        # Get item selections
        selection_input = input(
            "Enter the IDs of the items you wish to purchase, separated by commas (e.g., 1, 3, 5): "
        ).strip()
        
        selected_ids = []
        if selection_input:
            try:
                selected_ids = [int(item_id.strip()) for item_id in selection_input.split(',')]
            except ValueError:
                print("\nInvalid selection format. Please enter only numbers separated by commas.")
                return {}, 0.0

        # Build the cart based on valid selections
        for item_id in selected_ids:
            if item_id in catalog:
                item_info = catalog[item_id]
                # Note: If item name is duplicated (e.g., buying two laptops), 
                # this simple structure would overwrite the price. 
                # For simplicity, we assume unique purchases of items from the catalog.
                cart_items[item_info['name']] = item_info['price']
            else:
                print(f"Warning: Item ID {item_id} not found in catalog and was skipped.")

        # Get custom discount
        custom_discount_percent = float(input("\nEnter the custom discount percentage to apply (e.g., 10 for 10%): "))
        if custom_discount_percent < 0:
            print("Discount must be non-negative. Setting to 0%.")
            custom_discount_percent = 0.0

    except ValueError:
        print("\nInvalid input detected for discount. Please enter a number only.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {e}")
        sys.exit(1)

    return cart_items, custom_discount_percent

# Main execution block
if __name__ == "__main__":
    print("Welcome to the E-Commerce Cart System Calculator.")

    # 1. Display list and get user selection/discount
    user_cart_items, user_custom_discount = get_user_input(CATALOG)

    # Display the selected items for confirmation
    if user_cart_items:
        print("\n--- Cart Contents for Calculation ---")
        for name, price in user_cart_items.items():
            print(f"- {name}: ${price:,.2f}")
        print("-------------------------------------")
        
        # 2. Calculate and display the final total
        final_price = calculate_cart_total(user_cart_items, user_custom_discount)

        # 3. Display the final output
        print("\n====================================")
        print(f"FINAL TOTAL PRICE: ${final_price:,.2f}")
        print("====================================")
    else:
        print("\nNo items were selected for purchase.")