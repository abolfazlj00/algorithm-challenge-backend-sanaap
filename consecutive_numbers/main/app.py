def has_n_consecutive_ones_circular(binary_str: str, n: int) -> bool:
    """
    Check whether a binary string contains `n` consecutive '1's,
    considering circular rotation (end connected to start).

    Args:
        binary_str (str): Input binary string (e.g., '1010111'). Must contain only '0' and '1'.
        n (int): Number of consecutive '1's to search for. Must be >= 1.

    Returns:
        bool: True if there are `n` consecutive '1's in the circular string, otherwise False.

    Raises:
        ValueError: If n < 1, or binary_str contains characters other than '0' and '1'.
    """
    if n < 1:
        raise ValueError("n must be >= 1")
    if any(ch not in {"0", "1"} for ch in binary_str):
        raise ValueError("binary_str must contain only '0' and '1' characters")

    if n > len(binary_str):
        return False

    circular = binary_str + binary_str
    target = "1" * n
    return target in circular

if __name__ == "__main__":
    while True:
        binary_str = input("Enter a bynary-string (or type 'exit' to quit): ")
        if binary_str.lower() == "exit":
            break
        n = int(input("Enter n (number of consecutive 1s to check for): "))
        try:
            has_consecutive = has_n_consecutive_ones_circular(binary_str, n)
            print(f"Contains {n} consecutive 1s (circular): {has_consecutive}")
        except ValueError as e:
            print(f"Error: {e}")
            continue