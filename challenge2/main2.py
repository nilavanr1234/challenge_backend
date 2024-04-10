import json
from collections import Counter
from typing import List, Tuple

def load_data(filename: str) -> List[int]:
    """Load a list of integers from a JSON file."""
    # TODO: Implement loading the list of numbers from a JSON file named `filename`.
    pass  # placeholder

def calculate_frequency(numbers: List[int]) -> List[Tuple[int, int]]:
    """Calculate the frequency of each unique number and return sorted by frequency descending."""
    # TODO: Use collections.Counter to calculate frequency and sort by frequency (descending).
    pass  # placeholder

def get_third_highest_frequency(frequencies: List[Tuple[int, int]]) -> Tuple[int, int]:
    """Retrieve the third highest frequency from the list of (number, frequency) tuples."""
    # TODO: Implement logic to find the third highest frequency or handle case with less unique numbers.
    pass  # placeholder

def save_output(data: dict, filename: str) -> None:
    """Save the given data as JSON in a file."""
    # TODO: Implement saving the data to a JSON file named `filename`.
    pass  # placeholder

def main():
    numbers = load_data('data.json')
    frequencies = calculate_frequency(numbers)
    third_highest_freq = get_third_highest_frequency(frequencies)
    
    output = {
        "sorted_frequency_distribution": frequencies,
        "third_highest_frequency": third_highest_freq
    }
    
    save_output(output, 'output.json')
    
    print("Output saved to output.json")

if __name__ == "__main__":
    main()