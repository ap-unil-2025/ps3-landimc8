"""
Problem 4: File Word Counter
Process text files and perform various analyses.
"""

def create_sample_file(filename="sample.txt"):
    """
    Create a sample text file for testing.

    Args:
        filename (str): Name of the file to create
    """
    content = """Python is a powerful programming language.
It is widely used in web development, data science, and automation.
Python's simple syntax makes it great for beginners.
Many companies use Python for their projects.
Python can be helpful for trading and/or analysis because it can easily calculate, graph, and visualise data. Instead of clicking and formatting in Excel, you may load and create any plot with just two lines of code."""

    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")


def count_words(filename):
    """Count total words in the file."""
    with open(filename, 'r') as f:
        content = f.read()
    
    # Use split() to separate words by whitespace
    words = content.split()
    return len(words)


def count_lines(filename):
    """
    Count total lines in the file, only counting non-empty lines with content.
    """
    count = 0
    
    # Open the file
    with open(filename, 'r') as f:
        # Read all lines into a list
        lines = f.readlines()
        
        # Iterate through the lines list
        for line in lines:
            # Check if the line has any actual non-whitespace content.
            # .strip() removes all whitespace (spaces, tabs, newlines).
            if line.strip(): 
                count += 1
                
    return count



def count_characters(filename, include_spaces=True):
    """Count characters in the file."""
    with open(filename, 'r') as f:
        content = f.read()

    if not include_spaces:
        # Remove all whitespace characters (spaces, newlines, tabs)
        content = "".join(content.split()) 

    return len(content)


def find_longest_word(filename):
    """Find and return the longest word in the file."""
    import string
    
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Replace punctuation with a space or remove it
    # This ensures words like "automation." are treated as "automation"
    for char in string.punctuation:
        content = content.replace(char, '')

    words = content.split()
    
    if not words:
        return "" # Handle empty file

    # 2. Find the longest word using the max function and 'key=len'
    longest_word = max(words, key=len)
    
    return longest_word


def word_frequency(filename):
    """Return a dictionary of word frequencies."""
    import string
    frequency = {}
    
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Prepare content: lowercase and remove punctuation
    content = content.lower()
    for char in string.punctuation:
        content = content.replace(char, '')

    words = content.split()
    
    # 2. Count frequency
    for word in words:
        if word: # Ensure no empty strings from multiple spaces
            frequency[word] = frequency.get(word, 0) + 1
            
    return frequency


def analyze_file(filename):
    """
    Perform complete analysis of the file.

    Args:
        filename (str): Name of the file to analyze
    """
    print(f"\nAnalyzing: {filename}")
    print("-" * 40)

    try:
        # Display all analyses
        print(f"Lines: {count_lines(filename)}")
        print(f"Words: {count_words(filename)}")
        print(f"Characters (with spaces): {count_characters(filename, True)}")
        print(f"Characters (without spaces): {count_characters(filename, False)}")
        print(f"Longest word: {find_longest_word(filename)}")

        # Display top 5 most common words
        print("\nTop 5 most common words:")
        freq = word_frequency(filename)

        # Sort by frequency and get top 5
        top_words = sorted(freq.items(), key=lambda x: x[1], reverse=True)[:5]
        for word, count in top_words:
            print(f"  '{word}': {count} times")

    except FileNotFoundError:
        print(f"Error: File '{filename}' not found!")
    except Exception as e:
        print(f"Error: {e}")


def main():
    """Main function to run the file analyzer."""
    # Create sample file
    create_sample_file()

    # Analyze the sample file
    analyze_file("sample.txt")

    # Allow user to analyze their own file
    print("\n" + "=" * 40)
    user_file = input("Enter a filename to analyze (or press Enter to skip): ").strip()
    if user_file:
        analyze_file(user_file)


if __name__ == "__main__":
    main()