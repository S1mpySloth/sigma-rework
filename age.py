from datetime import datetime


def calculate_age(chosen_date):

    present_date = datetime.today()

    age = present_date.year - chosen_date.year - \
        ((present_date.month, present_date.day)
         < (chosen_date.month, chosen_date.day))

    return age


chosen_date = datetime(1999, 7, 21)  # enter desired date
age = calculate_age(chosen_date)
print(f"Age: {age}")
