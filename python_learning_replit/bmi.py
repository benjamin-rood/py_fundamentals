"""BMI calculator module.

Provides functions to calculate and categorize Body Mass Index.
This module is used throughout the Python Foundations course
starting in Week 5.
"""


def calculate_bmi(weight_kg, height_m):
    """Calculate Body Mass Index.

    Args:
        weight_kg: Patient's weight in kilograms
        height_m: Patient's height in meters

    Returns:
        BMI as a float, or None if inputs are invalid
    """
    if not isinstance(weight_kg, (int, float)) or not isinstance(height_m, (int, float)):
        return None
    if weight_kg <= 0 or height_m <= 0:
        return None
    return weight_kg / (height_m ** 2)


def categorize_bmi(bmi):
    """Categorize a BMI value.

    Args:
        bmi: BMI value as a float

    Returns:
        Category string: 'underweight', 'normal', 'overweight', or 'obese'

    Raises:
        ValueError: If bmi is not a positive number
    """
    if not isinstance(bmi, (int, float)) or bmi < 0:
        raise ValueError(f"BMI must be a non-negative number, got {bmi}")
    if bmi < 18.5:
        return "underweight"
    elif bmi < 25:
        return "normal"
    elif bmi < 30:
        return "overweight"
    else:
        return "obese"


if __name__ == "__main__":
    # This code only runs when you execute: python bmi.py
    # It does NOT run when another file imports this module
    test_bmi = calculate_bmi(70, 1.75)
    print(f"Test BMI: {test_bmi:.1f}")
    print(f"Category: {categorize_bmi(test_bmi)}")
