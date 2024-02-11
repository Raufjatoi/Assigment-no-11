# 3. Hydration Helper: Design a program that prompts the user for their weight and desired level of 
# hydration (e.g., light, moderate, intense exercise). Use nested if-else statements to suggest the 
# amount of water they should drink throughout the day.

def hydration_helper(weight, exercise_intensity):
    if exercise_intensity == "light":
        water_needed = weight * 0.03
    elif exercise_intensity == "moderate":
        water_needed = weight * 0.04
    elif exercise_intensity == "intense":
        water_needed = weight * 0.05
    else:
        return "Invalid input for exercise intensity."

    return f"To stay hydrated, you should drink about {water_needed:.2f} liters of water throughout the day."

weight = float(input("Enter your weight in kilograms: "))
exercise_intensity = input("Enter your exercise intensity (light, moderate, intense): ")

print(hydration_helper(weight, exercise_intensity))
