# main/artificial_pancreas.py

class ArtificialPancreasSystem:
    """A simplified model for data-driven glucose regulation."""

    GLUCOSE_PER_CARB = 0.5      # fixed increase per carb unit
    GLUCOSE_BURN_PER_MIN = 0.3  # fixed decrease per minute of exercise
    MIN_GLUCOSE = 60            # safety floor (set to 60 for uniqueness)

    def __init__(self, glucose_level, insulin_sensitivity=1.0, target_glucose=100, tolerance=10):
        self.glucose_level = glucose_level
        self.insulin_sensitivity = insulin_sensitivity
        self.target_glucose = target_glucose
        self.tolerance = tolerance
        self.total_insulin_delivered = 0

    def meal(self, carbs: float):
        """Simulate a meal event (input: carbs)."""
        if carbs < 0:
            raise ValueError("Carbs cannot be negative")
        self.glucose_level += carbs * self.GLUCOSE_PER_CARB

    def exercise(self, duration: float):
        """Simulate physical activity (input: duration in minutes)."""
        if duration < 0:
            raise ValueError("Exercise duration cannot be negative")
        self.glucose_level -= duration * self.GLUCOSE_BURN_PER_MIN
        # Prevent glucose from dropping below safe minimum
        if self.glucose_level < self.MIN_GLUCOSE:
            self.glucose_level = self.MIN_GLUCOSE
        return f"Exercise done and the new glucose level is {self.glucose_level}"

    def predict_action(self):
        """
        Predict and apply an appropriate system action.
        Returns (action, glucose_level).
        """
        if self.glucose_level > self.target_glucose + self.tolerance:
            # Too high → deliver insulin
            excess = self.glucose_level - self.target_glucose
            dose = excess * self.insulin_sensitivity
            self.glucose_level -= dose
            self.total_insulin_delivered += dose
            return f"Glucose level is getting high ({self.glucose_level+dose}), insulin amount of {dose} is needed to drop your Glucose level back to {self.glucose_level}"

        elif self.glucose_level < self.target_glucose - self.tolerance:
            # Too low, warning
            return f"Glucose level is getting low ({self.glucose_level}), you need to take Carbs of {(self.target_glucose - self.glucose_level)/0.5}"
        else:
            # Stable, maintain
            return f"Glucose level is currently {self.glucose_level}, so maintain your  ", self.glucose_level
        
ojo_diabetics = ArtificialPancreasSystem(125, 1, 100, 10)

ojo_diabetics.predict_action

print(ojo_diabetics.predict_action())