"""Tests for the bmi module.

Run with: pytest -v
"""

import pytest
from bmi import calculate_bmi, categorize_bmi


# --- Tests for calculate_bmi ---

def test_normal_bmi():
    """BMI for a 70kg, 1.75m person should be about 22.9."""
    result = calculate_bmi(70, 1.75)
    assert 22.8 < result < 23.0


def test_different_values():
    """BMI for a 90kg, 1.80m person should be about 27.8."""
    result = calculate_bmi(90, 1.80)
    assert 27.7 < result < 27.9


def test_zero_height_returns_none():
    """Zero height should return None, not crash."""
    assert calculate_bmi(70, 0) is None


def test_negative_height_returns_none():
    """Negative height should return None."""
    assert calculate_bmi(70, -1.75) is None


def test_zero_weight_returns_none():
    """Zero weight should return None."""
    assert calculate_bmi(0, 1.75) is None


def test_negative_weight_returns_none():
    """Negative weight should return None."""
    assert calculate_bmi(-70, 1.75) is None


def test_non_numeric_weight_returns_none():
    """String weight should return None, not crash."""
    assert calculate_bmi("seventy", 1.75) is None


def test_non_numeric_height_returns_none():
    """String height should return None, not crash."""
    assert calculate_bmi(70, "tall") is None


# --- Tests for categorize_bmi ---

def test_categorize_underweight():
    assert categorize_bmi(17.0) == "underweight"


def test_categorize_normal():
    assert categorize_bmi(22.0) == "normal"


def test_categorize_overweight():
    assert categorize_bmi(27.0) == "overweight"


def test_categorize_obese():
    assert categorize_bmi(35.0) == "obese"


# Boundary tests — these are where bugs hide

def test_categorize_boundary_18_5():
    """18.5 is the lower boundary of 'normal'."""
    assert categorize_bmi(18.5) == "normal"


def test_categorize_boundary_25():
    """25.0 is the lower boundary of 'overweight'."""
    assert categorize_bmi(25.0) == "overweight"


def test_categorize_boundary_30():
    """30.0 is the lower boundary of 'obese'."""
    assert categorize_bmi(30.0) == "obese"


def test_categorize_negative_raises():
    """Negative BMI should raise ValueError."""
    with pytest.raises(ValueError):
        categorize_bmi(-5.0)
