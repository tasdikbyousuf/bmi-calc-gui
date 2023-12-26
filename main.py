def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI) based on weight (in kilograms) and height (in meters).

    Parameters:
    - weight (float): Body mass in kilograms.
    - height (float): Height in meters.

    Returns:
    - float: Calculated BMI.
    """
    bmi = weight / (height ** 2)
    return bmi

def get_bmi_category(bmi):
    """
    Determine BMI category based on the calculated BMI.

    Parameters:
    - bmi (float): Calculated BMI.

    Returns:
    - str: BMI category (e.g., "Underweight", "Normal", "Overweight", "Obese", "Morbidly Obese").
    """
    if bmi <= 18.5:
        return "Underweight"
    elif bmi <= 25:
        return "Normal"
    elif bmi <= 30:
        return "Overweight"
    elif bmi <= 35:
        return "Obese"
    else:
        return "Morbidly Obese"

def bmi_calculator():
    """
    Collect user input for weight and height, calculate BMI, and display the BMI category.

    Returns:
    - None: Prints the calculated BMI and BMI category.
    """
    weight = float(input("Enter body mass in kilograms: "))
    height = float(input("Enter height in meters: "))

    bmi = calculate_bmi(weight, height)
    bmi_category = get_bmi_category(bmi)

    print("BMI:", round(bmi, 2))
    print("Category:", bmi_category)

bmi_calculator()
