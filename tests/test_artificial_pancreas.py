import pytest
from main.artificial_pancreas import ArtificialPancreasSystem

@pytest.fixture #to avoid repetition of system object in each test functions 
def system():
    return ArtificialPancreasSystem(100, 1,100, 10)
def test_glucose_increases_after_meal(system):
    system.meal(20)  # 20 carbs
    assert system.glucose_level > 100


def test_glucose_decreases_after_exercise(system):
   
    system.exercise(30)  # 30 minutes exercise
    assert system.glucose_level < 100


def test_glucose_never_below_min(system):
    system.exercise(500)  # huge duration
    assert system.glucose_level >= system.MIN_GLUCOSE
