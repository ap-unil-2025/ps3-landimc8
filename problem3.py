"""
Problem 3: Number Analysis
Analyze a list of numbers provided by the user.
"""

def get_numbers_from_user():
    """
    Get numbers from user until they type 'done'.
    Return a list of numbers.

    Returns:
        list: List of numbers entered by user
    """
    numbers = []

    while True:
        user_input = input("Enter a number (or type 'done'): ")

        if user_input.lower() == 'done':
            break 

        try:
            number = float(user_input)
            numbers.append(number)
        
        except ValueError:
            print(f"'{user_input}' is not a valid number. Please try again.")

    return numbers


def analyze_numbers(numbers):
    """
    Analyze the list and return a dictionary with:
    - count: number of elements
    - sum: sum of all numbers
    - average: average value
    - minimum: smallest number
    - maximum: largest number
    - even_count: count of even numbers
    - odd_count: count of odd numbers

    Args:
        numbers (list): List of numbers to analyze

    Returns:
        dict: Dictionary with analysis results, or None if list is empty
    """
    if not numbers:
        return None

    analysis = {}

    # Calculate basic statistics
    analysis['count'] = len(numbers)
    analysis['sum'] = sum(numbers)
    analysis['average'] = analysis['sum'] / analysis['count']
    analysis['minimum'] = min(numbers)
    analysis['maximum'] = max(numbers)

    # Count even/odd numbers (only for integers)
    even_count = 0
    odd_count = 0

    for num in numbers:
        # Check if the number is an exact integer
        if num == int(num): 
            if int(num) % 2 == 0:
                even_count += 1
            else:
                odd_count += 1

    analysis['even_count'] = even_count
    analysis['odd_count'] = odd_count

    return analysis


def display_analysis(analysis):
    """
    Display the analysis in a formatted way.
    """
    if not analysis:
        # This handles the case if no numbers were entered
        return

    print("\nAnalysis Results:")
    print("-" * 20)
    
    # Display all analysis results in a nice format, rounded to 2 decimals
    print(f"Count:    {analysis['count']}")
    print(f"Sum:      {analysis['sum']:.2f}") 
    print(f"Average:  {analysis['average']:.2f}") 
    print(f"Minimum:  {analysis['minimum']:.2f}")
    print(f"Maximum:  {analysis['maximum']:.2f}")
    print(f"Even Count: {analysis['even_count']}")
    print(f"Odd Count:  {analysis['odd_count']}")


def main():
    """Main function to run the number analyzer."""
    print("Number Analyzer")
    print("Enter numbers one at a time. Type 'done' when finished.")
    print()

    # Get numbers from user
    numbers = get_numbers_from_user()

    if not numbers:
        print("No numbers entered!")
        return

    # Analyze the numbers
    analysis = analyze_numbers(numbers)

    # Display the results
    display_analysis(analysis)


if __name__ == "__main__":
    main()