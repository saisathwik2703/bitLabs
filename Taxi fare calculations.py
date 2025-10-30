"""
Program to calculate taxi fares based on a base rate and distance rate.
"""

# --- Configuration ---
BASE_FARE = 50  # Base charge for any trip (in dollars)
RATE_PER_KM = 10  # Charge per kilometer (in dollars)

# --- Function to Calculate Single Trip Fare ---

def calculate_trip_fare(distance_km):
    """
    Calculates the total fare for a single trip.
    
    Formula: Fare = BASE_FARE + (Distance * RATE_PER_KM)

    Args:
        distance_km (float or int): The distance of the trip in kilometers.

    Returns:
        int: The total calculated fare.
    """
    # Ensure distance is non-negative
    if distance_km < 0:
        return 0
        
    distance_charge = distance_km * RATE_PER_KM
    total_fare = BASE_FARE + distance_charge
    return total_fare

# --- Main Program Execution ---

def analyze_trips(trips):
    """
    Calculates and displays the fare for multiple trips and the grand total.

    Args:
        trips (list): A list of trip distances in kilometers.
    """
    print("\n--- Taxi Fare Calculation ---")
    print(f"Rates: Base Fare = ${BASE_FARE}, Distance Rate = ${RATE_PER_KM}/km")
    print("-" * 30)

    total_fare_for_all_trips = 0

    if not trips:
        print("No valid trips were entered for analysis.")
        print("=" * 30)
        return

    for i, distance in enumerate(trips):
        # Calculate fare using the dedicated function
        fare = calculate_trip_fare(distance)
        total_fare_for_all_trips += fare
        
        # Display individual trip result
        print(f"Trip {i + 1}: ${fare} ({distance} km)")
        
    print("-" * 30)
    # Display the grand total
    print(f"Total Fare: ${total_fare_for_all_trips}")
    print("=" * 30)

def get_user_trips():
    """
    Prompts the user to enter trip distances, parses the input, and
    returns a list of valid float distances.
    """
    print("\n--- Interactive Trip Data Entry ---")
    user_input = input("Enter trip distances in km (e.g., 5, 10.5, 3): ").strip()
    
    if not user_input:
        print("No input provided.")
        return []

    # Split the input by comma and filter out empty strings
    raw_distances = [item.strip() for item in user_input.split(',') if item.strip()]
    
    valid_distances = []
    
    for item in raw_distances:
        try:
            distance = float(item)
            # Only include non-negative distances
            if distance >= 0:
                valid_distances.append(distance)
            else:
                print(f"⚠️ Warning: Negative distance '{item}' skipped. Distance must be non-negative.")
        except ValueError:
            print(f"❌ Error: Input '{item}' is not a valid number and was skipped.")
            
    return valid_distances


if __name__ == "__main__":
    # 1. Applying the input example condition first
    example_trips = [5, 10, 3]
    print("\n--- Running Example Condition ---")
    analyze_trips(example_trips)

    # 2. Then switching to interactive mode to take input from the user
    print("\n\n--- Interactive User Input Mode ---")
    trip_distances = get_user_trips()
    analyze_trips(trip_distances)
