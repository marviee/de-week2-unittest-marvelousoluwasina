# Artificial Pancreas System – Week 2 Unit Testing

This project is a simplified prototype of an Artificial Pancreas System, built with Python.  
It simulates how glucose levels respond to meals and exercise, and how insulin delivery can help maintain balance.

# Features
- Simulates glucose changes after meals and exercise
- Predicts actions: `deliver_insulin`, `warn_low_glucose`, or `maintain`
- Tracks total insulin delivered
- Prevents glucose from dropping below a safe minimum
- Includes **pytest unit tests** for correctness and stability

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