import pytest
from task2 import *

def test_bmi_normal():
    assert calculate_bmi(1.8, 70) == "Маса тіла в нормі"

def test_bmi_underweight():
    assert calculate_bmi(1.6, 45) == "Недостатня вага"

def test_bmi_overweight():
    assert calculate_bmi(1.7, 85) == "Слідкуйте за фігурою"

def test_bmi_invalid_height_zero():
    with pytest.raises(ValueError):
        calculate_bmi(0, 70)

def test_bmi_invalid_weight_negative():
    with pytest.raises(ValueError):
        calculate_bmi(1.8, -10)

def test_bmi_boundary_underweight():
    assert calculate_bmi(1.8, 59.94) == "Недостатня вага"

def test_bmi_boundary_normal():
    assert calculate_bmi(1.8, 80.99) == "Маса тіла в нормі"
