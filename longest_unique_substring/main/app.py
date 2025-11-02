
def longest_unique_substring(input_string: str) -> str:
    """
    Find the longest substring without repeating characters.

    Args:
        input_string (str): The input string to be analyzed.

    Returns:
        str: The longest substring that contains no repeated characters.
    """

if __name__ == "__main__":
    while True:
        input_string = input("Enter a string (or type 'exit' to quit): ")
        if input_string.lower() == "exit":
            break
        print(f"The longest unique substring in your input is: {longest_unique_substring(input_string)}")