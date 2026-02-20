from datetime import datetime
import uuid

def parse_date(date_str, optional=False):
    if optional and not date_str:
        return None
    try:
        return datetime.strptime(date_str, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return parse_date(input("Enter date again: "), optional)

def generate_id():
    return str(uuid.uuid4())[:8]
