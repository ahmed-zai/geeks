""" Temperature Advice

Goal: Generate a random temperature and provide advice based on the temperature range.

Key Python Topics:

    Functions
    Conditionals (if / elif)
    Random numbers
    Floating-point numbers (Bonus)
    Handling seasons (Bonus)


Step 1: Create the get_random_temp() Function

    Create a function called get_random_temp() that returns a random integer between -10 and 40 degrees Celsius.


Step 2: Create the main() Function

    Create a function called main(). Inside this function:
        Call get_random_temp() to get a random temperature.
        Store the temperature in a variable and print a friendly message like:
        “The temperature right now is 32 degrees Celsius.”


Step 3: Provide Temperature-Based Advice

    Inside main(), provide advice based on the temperature:
        Below 0°C: e.g., “Brrr, that’s freezing! Wear some extra layers today.”
        Between 0°C and 16°C: e.g., “Quite chilly! Don’t forget your coat.”
        Between 16°C and 23°C: e.g., “Nice weather.”
        Between 24°C and 32°C: e.g., “A bit warm, stay hydrated.”
        Between 32°C and 40°C: e.g., “It’s really hot! Stay cool.”


Step 4: Floating-Point Temperatures (Bonus)

    Modify get_random_temp() to return a random floating-point number using random.uniform() for more accurate temperature values.


Step 5: Month-Based Seasons (Bonus)

    Instead of directly generating a random temperature, ask the user for a month (1-12) and determine the season using if/elif conditions.
        Modify get_random_temp() to return temperatures specific to each season.


Expected Output:

The temperature right now is 32 degrees Celsius.
It's really hot! Stay cool.
"""

import random


def get_random_temp(season):
    match season:
        case "winter":
            return round(random.uniform(-10, 10), 1)
        case "spring":
            return round(random.uniform(10, 20), 1)
        case "summer":
            return round(random.uniform(20, 40), 1)
        case "autumn":
            return round(random.uniform(10, 20), 1)
        case _:
            return round(random.uniform(-10, 40), 1)


def get_season_by_month(month):
    match month:
        case 12 | 1 | 2:
            return "winter"
        case 3 | 4 | 5:
            return "spring"
        case 6 | 7 | 8:
            return "summer"
        case 9 | 10 | 11:
            return "autumn"
        case _:
            return None

# 
def main():
    try:
        month = int(input("Enter the month number (1–12): "))
        season = get_season_by_month(month)

        if not season:
            print(" Invalid month.")
            return

        temp = get_random_temp(season)
        print(f"\n🌡️ The temperature right now is {temp}°C.")

        match temp:
            case t if t < 0:
                print("Brrr, that’s freezing! Wear some extra layers today.")
            case t if 0 <= t < 16:
                print("Quite chilly! Don’t forget your coat.")
            case t if 16 <= t < 24:
                print("Nice weather.")
            case t if 24 <= t < 32:
                print("A bit warm, stay hydrated.")
            case t if 32 <= t <= 40:
                print("It’s really hot! Stay cool.")
            case _:
                print("Temperature out of expected range.")
    except ValueError:
        print("Please enter a valid number.")

main()
