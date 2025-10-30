# --- Configuration ---
ROWS = ['A', 'B', 'C']  # A is the front row (down), C is the back row (up)
SEATS_PER_ROW = 5
TOTAL_SEATS = len(ROWS) * SEATS_PER_ROW
# Initial booked seats are stored as a set of (row, seat_number) tuples for fast lookup.
# Example: ('A', 2) means Row A, Seat 2 is booked.
booked_seats = {('A', 2), ('B', 5), ('C', 1)} 

# --- Functions for Seat Management ---

def get_available_seats():
    """
    Calculates and returns a list of available (row, seat) tuples.
    """
    available_seats = []
    for row in ROWS:
        for seat in range(1, SEATS_PER_ROW + 1):
            seat_tuple = (row, seat)
            if seat_tuple not in booked_seats:
                available_seats.append(seat_tuple)
    return available_seats

def book_seat(row_label, seat_number):
    """
    Attempts to book a specific seat.
    """
    seat_tuple = (row_label, seat_number)
    
    if row_label not in ROWS or not (1 <= seat_number <= SEATS_PER_ROW):
        print(f"❌ Error: Seat {row_label}{seat_number} is an invalid seat identifier.")
        return False
        
    if seat_tuple in booked_seats:
        print(f"❌ Error: Seat {row_label}{seat_number} is ALREADY booked.")
        return False
    else:
        # Book the seat
        booked_seats.add(seat_tuple)
        print(f"✅ Success: Seat {row_label}{seat_number} has been booked.")
        return True

def cancel_seat(row_label, seat_number):
    """
    Attempts to cancel a booking for a specific seat.
    """
    seat_tuple = (row_label, seat_number)
    
    if row_label not in ROWS or not (1 <= seat_number <= SEATS_PER_ROW):
        print(f"❌ Error: Seat {row_label}{seat_number} is an invalid seat identifier.")
        return False
        
    if seat_tuple in booked_seats:
        # Cancel the booking (remove the seat tuple)
        booked_seats.remove(seat_tuple)
        print(f"✅ Success: Booking for seat {row_label}{seat_number} has been CANCELLED.")
        return True
    else:
        print(f"❌ Error: Seat {row_label}{seat_number} is not currently booked, so it cannot be cancelled.")
        return False

def display_status():
    """
    Prints the current status of the cinema hall with a visual map.
    """
    print("\n" + "=" * 60)
    print("CINEMA HALL STATUS")
    print("-" * 60)

    # 1. Visual Map
    print("  ")
    print("  SEATING MAP (A=Front, C=Back):")
    
    # Print seat numbers header
    header = "  Row |" + " ".join(f"{i:^3}" for i in range(1, SEATS_PER_ROW + 1)) + " |"
    print(header)
    print("  " + "-" * len(header))

    # Print rows
    for row in ROWS:
        row_display = f"  {row}   |"
        for seat in range(1, SEATS_PER_ROW + 1):
            if (row, seat) in booked_seats:
                # Booked seat: X
                row_display += " [X] "
            else:
                # Available seat: O
                row_display += " [O] "
        print(row_display + " |")

    # 2. Summary
    booked_list = sorted([f"{r}{s}" for r, s in booked_seats])
    available_list = sorted([f"{r}{s}" for r, s in get_available_seats()])
    
    print("\n" + "-" * 60)
    print(f"Total Seats: {TOTAL_SEATS}")
    print(f"Seats Booked ({len(booked_seats)}): {', '.join(booked_list)}")
    print(f"Seats Available ({len(available_list)}): {', '.join(available_list)}")
    print("=" * 60 + "\n")


# --- Main Program Execution ---

print("--- Interactive Row-Based Booking Simulator ---")
print(f"The cinema has {len(ROWS)} rows ({ROWS[0]} to {ROWS[-1]}) with {SEATS_PER_ROW} seats each.")
print("Remember: Row A is the front (down), Row C is the back (up).\n")

while True:
    # Display current status at the beginning of each loop
    display_status()
    
    # Display Menu
    print("Please select an action:")
    print("1: Book Seat(s)")
    print("2: Cancel a Booking")
    print("3: Exit System")
    
    # Get user choice
    try:
        choice = int(input("Enter your choice (1-3): "))
    except ValueError:
        print("❌ Invalid input. Please enter a number from 1 to 3.")
        continue # Skip the rest of the loop and start over

    # Process Choice
    if choice == 1:
        # Book Seat(s) - Now handles multiple seats
        try:
            # Prompt for multiple seats separated by commas
            user_input = input("Enter seat(s) to BOOK (e.g., C3, A1, B2): ").strip().upper()
            
            # Split the input by comma and clean up each entry
            seats_to_book = [s.strip() for s in user_input.split(',') if s.strip()]

            if not seats_to_book:
                 print("⚠️ No valid seats entered. Skipping booking.")
                 continue

            print(f"\nAttempting to book {len(seats_to_book)} seat(s)...")
            
            # Loop through all requested seats
            for seat_str in seats_to_book:
                if len(seat_str) < 2:
                    print(f"❌ Error: '{seat_str}' is too short. Please use format RowSeat (e.g., B4).")
                    continue
                
                try:
                    row = seat_str[0]
                    seat = int(seat_str[1:])
                    # Reuse existing single-seat booking logic
                    book_seat(row, seat) 
                except ValueError:
                    print(f"❌ Error: Seat number in '{seat_str}' is not a valid number.")
                except Exception as e:
                    # Catch any other parsing error
                    print(f"❌ An unexpected error occurred while processing '{seat_str}': {e}")
                    
        except Exception as e:
            print(f"❌ An error occurred during input processing: {e}")
            
    elif choice == 2:
        # Cancel a Booking (still handles one seat at a time)
        try:
            user_input = input("Enter the seat to CANCEL (e.g., A2 for Row A, Seat 2): ").strip().upper()
            row = user_input[0]
            seat = int(user_input[1:])
            cancel_seat(row, seat)
        except (IndexError, ValueError):
            print("❌ Invalid format. Please enter in the format: RowSeat (e.g., B4).")

    elif choice == 3:
        # Exit System
        print("\nThank you for using the booking system. Goodbye!")
        break
        
    else:
        print("❌ Invalid choice. Please select 1, 2, or 3.")
        
    print("\n" + "~" * 60 + "\n")