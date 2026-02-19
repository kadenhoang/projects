from datetime import datetime
from calendar import isleap

def is_leap_year(year):
    if (isleap(year)):
        return True
    else:
        return False
           
def calculate_age(birth_date): 
    today = datetime.today()
    age = today.year - birth_date.year

    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1

    return age

def calculate_age_in_months(birth_date):
    today = datetime.today()
    age_in_months = (today.year - birth_date.year) * 12 + (today.month - birth_date.month)

    if today.day < birth_date.day:
        age_in_months -= 1

    return age_in_months

def calculate_age_in_days(birth_date):
    today = datetime.today()
    age_in_days = (today - birth_date).days
    return age_in_days

def get_birthday_info():
    birth_date_str = input("Enter your birth date (YYYY-MM-DD): ")
    birth_date = datetime.strptime(birth_date_str, "%Y-%m-%d")
    return birth_date

def main():

    birth_date = get_birthday_info()
    
    age = calculate_age(birth_date)
    print(f"You are {age} years old.")
    
    age_in_months = calculate_age_in_months(birth_date)
    print(f"You are {age_in_months} months old.")

    age_in_days = calculate_age_in_days(birth_date)
    print(f"You are {age_in_days} days old.")
    
    if is_leap_year(birth_date.year):
        print(f"{birth_date.year} is a leap year.")
    else:
        print(f"{birth_date.year} is not a leap year.")

if __name__ == "__main__":
    main()