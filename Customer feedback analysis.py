"""
Program to calculate the percentage of positive customer feedback (ratings 4 or 5).
"""

def calculate_positive_percentage(ratings):
    """
    Calculates the percentage of positive feedback (ratings of 4 or 5)
    from a list of integer ratings.

    Args:
        ratings (list): A list of integer ratings (1-5).

    Returns:
        str: A formatted string showing the positive feedback percentage, 
             or a message if no ratings are available.
    """
    total_ratings = len(ratings)

    # Requirement: Handle cases where no ratings are available.
    if total_ratings == 0:
        return "No ratings available to calculate feedback percentage."

    # Identify positive feedback (ratings of 4 or 5)
    positive_count = 0
    for rating in ratings:
        if rating >= 4:
            positive_count += 1

    # Calculate percentage
    percentage = (positive_count / total_ratings) * 100

    # Format the output to one decimal place
    return f"Positive Feedback: {percentage:.1f}%"

# --- Main Program Execution for User Input ---

def get_user_ratings():
    """
    Prompts the user to enter customer ratings and validates the input.
    Returns a list of valid integer ratings.
    """
    print("\n--- Customer Feedback Analysis Tool ---")
    user_input = input("Enter customer ratings (1-5), separated by commas (e.g., 5, 4, 3, 5): ").strip()
    
    if not user_input:
        return []

    raw_ratings = [item.strip() for item in user_input.split(',')]
    processed_ratings = []
    errors_found = False

    for item in raw_ratings:
        if not item:
            continue
        try:
            rating = int(item)
            if 1 <= rating <= 5:
                processed_ratings.append(rating)
            else:
                print(f"⚠️ Warning: Rating '{item}' skipped. Ratings must be between 1 and 5.")
                errors_found = True
        except ValueError:
            print(f"❌ Error: Input '{item}' is not a valid number and was skipped.")
            errors_found = True

    if errors_found:
        print("Please review the warnings and errors above.")
        
    return processed_ratings


if __name__ == "__main__":
    ratings_list = get_user_ratings()

    print("\n" + "=" * 40)
    if ratings_list:
        print(f"Input Ratings: {ratings_list}")
        
    result = calculate_positive_percentage(ratings_list)
    print(result)
    print("=" * 40)
