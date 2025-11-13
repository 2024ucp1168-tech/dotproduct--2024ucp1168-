def get_vector_input(prompt):
    """
    Prompts the user to enter vector elements and returns them as a list of floats.
    """
    while True:
        try:
            elements_str = input(prompt + " (comma-separated numbers): ")
            elements = [float(e.strip()) for e in elements_str.split(',')]
            return elements
        except ValueError:
            print("Invalid input. Please enter numbers separated by commas.")

def calculate_dot_product(vec1, vec2):
    """
    Calculates the dot product of two vectors.
    Raises a ValueError if the vectors have different lengths.
    """
    if len(vec1) != len(vec2):
        raise ValueError("Vectors must have the same length to calculate the dot product.")
    
    dot_product = sum(v1 * v2 for v1, v2 in zip(vec1, vec2))
    return dot_product

if __name__ == "__main__":
    print("--- Dot Product Calculator ---")

    vector1 = get_vector_input("Enter elements for Vector 1")
    vector2 = get_vector_input("Enter elements for Vector 2")

    try:
        result = calculate_dot_product(vector1, vector2)
        print(f"\nThe dot product of {vector1} and {vector2} is: {result}")
    except ValueError as e:
        print(f"\nError: {e}")
