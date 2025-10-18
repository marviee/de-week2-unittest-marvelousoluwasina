# Artificial Pancreas System – Week 2 Unit Testing

This project is a simplified prototype of an Artificial Pancreas System, built with Python.  
It simulates how glucose levels respond to meals and exercise, and how insulin delivery can help maintain balance.

# Features
- Simulates glucose changes after meals and exercise
- Predicts actions: `deliver_insulin`, `warn_low_glucose`, or `maintain`
- Tracks total insulin delivered
- Prevents glucose from dropping below a safe minimum
- Includes **pytest unit tests** for correctness and stability

# Initialization Notes

The ArtificialPancreasSystem requires only one argument when creating a new system — the current glucose level.
Other parameters have default values, but you can override them if needed.

Constructor:

ArtificialPancreasSystem(glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10)


glucose_level is Required, the starting glucose value ...

insulin_sensitivity is Optional, defaults to 1.0.

target_glucose is Optional, defaults to 100mg/dL.

tolerance isOptional, defaults to 10.

Examples:

# Minimal setup (only required argument)
system = ArtificialPancreasSystem(100)

# Custom sensitivity and target
system = ArtificialPancreasSystem(120, insulin_sensitivity=0.8, target_glucose=110, tolerance = 10)

## Folder Structure
main/
artificial_pancreas.py
tests/
test_artificial_pancreas.py
README.md
requirements.txt
.gitignore

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/marviee/de-week2-unittest-marvelousoluwasina.git
   cd de-week2-unittest-marvelousoluwasina

(Optional) Create and activate a virtual environment:
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

Install dependencies in git bashh:
pip install -r requirements.txt

Run the tests:
in bash, pytest


Author

Marvelous Oluwasina
GitHub: @marviee