import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixtures #to avoid repetition of sys object in each test functions 
def sys():
    return ArtificialPancreasSystem(100, 1,100, 10)
def test_glucose_increases_after_meal():
    sys.meal(20)  # 20 carbs
    assert sys.glucose_level > 100


def test_glucose_decreases_after_exercise():
   
    sys.exercise(30)  # 30 minutes exercise
    assert sys.glucose_level < 100


def test_glucose_never_below_min():
    sys.exercise(500)  # huge duration
    assert sys.glucose_level >= sys.MIN_GLUCOSE
