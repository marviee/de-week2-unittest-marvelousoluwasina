import pytest
from main.artificial_pancreas import ArtificialPancreasSystem


def test_glucose_increases_after_meal():
    system = ArtificialPancreasSystem(glucose_level=100)
    system.meal(20)  # 20 carbs
    assert system.glucose_level > 100


def test_glucose_decreases_after_exercise():
    system = ArtificialPancreasSystem(glucose_level=120)
    system.exercise(30)  # 30 minutes exercise
    assert system.glucose_level < 120


def test_glucose_never_below_min():
    system = ArtificialPancreasSystem(glucose_level=100)
    system.exercise(500)  # huge duration
    assert system.glucose_level >= system.MIN_GLUCOSE
